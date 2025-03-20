import random
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("../Key/Firebase_key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def fetch_users():
    users_ref = db.collection("users").stream()
    return [{"uid": user.id, **user.to_dict()} for user in users_ref]

def fetch_places():
    places_ref = db.collection("places").stream()
    return [{"place_id": place.id, **place.to_dict()} for place in places_ref]

def generate_ratings(users, places):
    ratings = []
    for user in users:
        preferred_places = [p for p in places if p["place_type"] in user["preferences"]]
        num_ratings = random.randint(3, 7)
        selected_places = random.sample(places, min(num_ratings, len(places)))
        
        for place in selected_places:
            if place in preferred_places:
                rating = round(random.uniform(4.0, 5.0), 1)  # Higher for preferred places
            else:
                rating = round(random.uniform(2.0, 3.5), 1)  # Lower for non-preferred places
            
            ratings.append({
                "uid": user["uid"],
                "place_id": place["place_id"],
                "rating": rating
            })
    
    return ratings

def upload_ratings_to_firestore(ratings):
    ratings_ref = db.collection("ratings")
    for rating in ratings:
        ratings_ref.add(rating)
    print(f"Uploaded {len(ratings)} ratings to Firestore successfully!")

if __name__ == "__main__":
    users = fetch_users()
    places = fetch_places()
    ratings = generate_ratings(users, places)
    upload_ratings_to_firestore(ratings)
    
    # Save to JSON file as backup
    # with open("user_ratings.json", "w") as f:
    #     json.dump(ratings, f, indent=4)
    # print("Ratings data saved to user_ratings.json")
