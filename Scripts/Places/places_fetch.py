import requests
import firebase_admin
from firebase_admin import credentials, firestore
import os 
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase
cred = credentials.Certificate("../../Key/Firebase_key.json")  # Update with your Firebase key path
firebase_admin.initialize_app(cred)
db = firestore.client()

# Google Maps API Key
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")  # Replace with your actual API key

# Fixed location for testing (latitude, longitude)
LOCATION = "12.9716,77.5946"  # Example: Bangalore, India
PLACE_TYPES = ["tourist_attraction", "amusement_park", "museum", "zoo", "aquarium", "art_gallery", "park"]  # List of tourist-friendly place types

# Google Places API URL
PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

MIN_REVIEWS = 1000  # Minimum number of user reviews to filter places

def fetch_places():
    all_places = []
    for place_type in PLACE_TYPES:
        next_page_token = None
        while True:
            params = {
                "location": LOCATION,
                "radius": 50000,  # Increased radius to 100km
                "type": place_type,
                "key": GOOGLE_MAPS_API_KEY,
            }
            if next_page_token:
                params["pagetoken"] = next_page_token
            
            response = requests.get(PLACES_API_URL, params=params)
            data = response.json()
            
            if "results" in data:
                for place in data["results"]:
                    user_ratings_total = place.get("user_ratings_total", 0)
                    if user_ratings_total >= MIN_REVIEWS:  # Filter based on minimum reviews
                        place_data = {
                            "place_id": place["place_id"],
                            "name": place.get("name"),
                            "latitude": place["geometry"]["location"]["lat"],
                            "longitude": place["geometry"]["location"]["lng"],
                            "rating": place.get("rating", "N/A"),
                            "user_ratings_total": user_ratings_total,
                            "place_type": place_type
                        }
                        
                        if not is_duplicate(place_data["place_id"]):
                            all_places.append(place_data)
                            store_in_firestore(place_data)
                
            next_page_token = data.get("next_page_token")
            if not next_page_token:
                break  # Exit loop if no more pages
    return all_places

def is_duplicate(place_id):
    query = db.collection("places").where("place_id", "==", place_id).stream()
    return any(query)  # Returns True if place_id exists, False otherwise

def store_in_firestore(place_data):
    db.collection("places").add(place_data)
    print(f"Stored: {place_data['name']} ({place_data['place_type']})")

if __name__ == "__main__":
    fetched_places = fetch_places()
    print(fetched_places)
