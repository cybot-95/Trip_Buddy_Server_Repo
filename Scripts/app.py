from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import firebase_admin
from firebase_admin import credentials, firestore
import random
import os

# Set the maximum number of CPU cores to be used for parallel processing
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("Path to JSON Key")
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Load Saved Model and Data
model = joblib.load("../Model/recommendation_model.pkl")
places_pivot = joblib.load("../Model/places_pivot.pkl")

# Fetch Firestore data
def fetch_firestore_data(collection_name):
    collection_ref = db.collection(collection_name)
    docs = collection_ref.stream()
    return [doc.to_dict() for doc in docs]

# Load data
def load_data():
    places = fetch_firestore_data("places")
    users = fetch_firestore_data("users")
    ratings = fetch_firestore_data("ratings")
    return places, users, ratings

# Fetch User Preference
def get_user_preference(uid, ratings, places):
    user_ratings = [r for r in ratings if r["uid"] == uid]
    if not user_ratings:
        return None
    
    place_type_counts = {}

    for rating in user_ratings:
        place_id = rating["place_id"]
        place = next((p for p in places if p.get("place_id") == place_id), None)

        if not place:
            print(f"Warning: Place ID {place_id} not found in places dataset.")
            continue  # Skip missing places

        if "place_type" not in place:
            print(f"Warning: Place {place.get('name', 'Unknown')} does not have a place_type.")
            continue  # Skip if place_type is missing

        place_type = place["place_type"]
        place_type_counts[place_type] = place_type_counts.get(place_type, 0) + 1
    
    if not place_type_counts:
        print(f"No valid place types found for user {uid}")
        return None

    return max(place_type_counts, key=place_type_counts.get)

# Get Recommendations
def get_recommendations(uid=None, place_type=None):
    places, users, ratings = load_data()

    user_preference = get_user_preference(uid, ratings, places) if uid else None
    print("User Preference:", user_preference)

    if place_type:
        filtered_places = [p for p in places if p["place_type"] == place_type]
        print("place_type")
    elif user_preference:
        filtered_places = [p for p in places if p["place_type"] == user_preference]
        print("user_ref")
    else:
        # Default recommendation: Top-rated places
        filtered_places = sorted(places, key=lambda x: x.get("avg_rating", 0), reverse=True)[:5]
        print("default_recommendation")
        return {"recommendations": [p["name"] for p in filtered_places]}

    if not filtered_places:
        return {"error": "No places found for the selected category."}

    sample_place = random.choice(filtered_places)
    place_name = sample_place["name"]

    try:
        place_index = np.where(places_pivot.index == place_name)[0][0]
    except IndexError:
        return {"error": "Place not found! Try again with a different place."}

    dist, suggestions = model.kneighbors(places_pivot.iloc[place_index, :].values.reshape(1, -1), n_neighbors=5)
    return {"recommendations": [places_pivot.index[i] for i in suggestions.flatten()]}

# API Endpoint
@app.route("/recommend", methods=["GET"])
def recommend():
    uid = request.args.get("uid")
    place_type = request.args.get("place_type") # "tourist_attraction", "amusement_park", "museum", "zoo", "aquarium", "art_gallery", "park"

    recommendations = get_recommendations(uid=uid, place_type=place_type)
    print(uid, place_type, recommendations)
    return jsonify(recommendations)

# Health Check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Recommendation API is running"})

# Run Flask Server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
     