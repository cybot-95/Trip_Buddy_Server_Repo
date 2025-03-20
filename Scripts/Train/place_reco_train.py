import random
import numpy as np
import firebase_admin
from firebase_admin import credentials, firestore
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import os
import joblib

# Set the maximum number of CPU cores to be used for parallel processing
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  

# Load Firebase credentials
cred = credentials.Certificate("../Key/Firebase_key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Fetch data from Firestore
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

# Get user's most preferred place type
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

# Prepare data for recommendation
def prepare_recommendation_data():
    places, users, ratings = load_data()
    ratings_df = pd.DataFrame(ratings)
    places_df = pd.DataFrame(places)
    places_df.rename(columns={"rating": "avg_rating"}, inplace=True)
    
    # Merge ratings with places
    ratings_places = ratings_df.merge(places_df, on="place_id")
    num_rating = ratings_places.groupby('name')['rating'].count().reset_index()
    num_rating.rename(columns={"rating": "no_of_ratings"}, inplace=True)
    final_rating = ratings_places.merge(num_rating, on='name')
    final_rating.drop_duplicates(['uid', 'name'], inplace=True)
    
    # Pivot table
    places_pivot = final_rating.pivot_table(values='rating', index='name', columns='uid')
    places_pivot.fillna(0, inplace=True)
    
    return places_pivot, places, ratings

# Build and train model
def train_model():
    places_pivot, _, _ = prepare_recommendation_data()
    places_sparse = csr_matrix(places_pivot)
    model = NearestNeighbors(algorithm='brute')
    model.fit(places_sparse)

    

    return model, places_pivot

def save_model():
    model, places_pivot = train_model()
    # Save the model and data
    joblib.dump(model, "recommendation_model.pkl")
    joblib.dump(places_pivot, "places_pivot.pkl")
    print("✅ Model and data saved successfully!")


# Get recommendations based on user preference, place type, or similar users
def get_recommendations(uid=None, place_type=None):
    places_pivot, places, ratings = prepare_recommendation_data()
    
    if uid:
        user_preference = get_user_preference(uid, ratings, places)
    else:
        user_preference = None
    
    if place_type:
        filtered_places = [p for p in places if p["place_type"] == place_type]
    elif user_preference:
        filtered_places = [p for p in places if p["place_type"] == user_preference]
    else:
        # Default recommendation: Top-rated places
        filtered_places = sorted(places, key=lambda x: x.get("avg_rating", 0), reverse=True)[:5]
        return [p["name"] for p in filtered_places]
    
    if not filtered_places:
        return "No places found for the selected category."
    
    sample_place = random.choice(filtered_places)
    place_name = sample_place["name"]
    
    try:
        place_index = np.where(places_pivot.index == place_name)[0][0]
    except IndexError:
        return "Place not found! Try again with a different place."
    
    model, _ = train_model()
    dist, suggestions = model.kneighbors(places_pivot.iloc[place_index, :].values.reshape(1, -1), n_neighbors=5)
    return [places_pivot.index[i] for i in suggestions.flatten()]

# Debugging: Print recommendations
if __name__ == "__main__":
    #save_model()
    test_uid = 100  # Replace with an actual user ID
    test_place_type = None  # "tourist_attraction", "amusement_park", "museum", "zoo", "aquarium", "art_gallery", "park"
    print(f"Recommendations for User {test_uid} and Place Type {test_place_type}:")
    recommendations = get_recommendations(uid=test_uid, place_type=test_place_type)
    print(recommendations)
