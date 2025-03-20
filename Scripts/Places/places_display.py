import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("../../Key/Firebase_key.json")  # Update with correct path
firebase_admin.initialize_app(cred)
db = firestore.client()

def fetch_and_display_places():
    place_types = ["tourist_attraction", "amusement_park", "museum", "zoo", "aquarium", "art_gallery", "park"]  # Ordered place types
    places_by_type = {}
    
    for place_type in place_types:
        query = db.collection("places").where("place_type", "==", place_type).stream()
        places = [{"name": doc.to_dict().get("name"),
                   "latitude": doc.to_dict().get("latitude"),
                   "longitude": doc.to_dict().get("longitude"),
                   "rating": doc.to_dict().get("rating"),
                   "user_ratings_total": doc.to_dict().get("user_ratings_total")}
                  for doc in query]
        
        if places:
            places_by_type[place_type] = places
    
    # Display results
    for place_type, places in places_by_type.items():
        print(f"\nPlaces under {place_type}:")
        for place in places:
            print(f"- {place['name']} (Rating: {place['rating']}, Reviews: {place['user_ratings_total']})")

if __name__ == "__main__":
    fetch_and_display_places()
