import random
import json
from faker import Faker
import firebase_admin
from firebase_admin import credentials, firestore
# from google.cloud import firestore
# import firebase_admin
# from firebase_admin import credentials


# Load Firebase credentials
cred = credentials.Certificate("../Key/Firebase_key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Initialize Faker for realistic names
fake = Faker()

# Define possible place categories
PLACE_CATEGORIES = ["amusement_park", "museum", "tourist_attraction", "zoo", "aquarium", "art_gallery", "park"]

# Function to generate a random user
def generate_user(uid):
    name = fake.name()
    age = random.randint(18, 60)
    preferences = random.sample(PLACE_CATEGORIES, k=random.randint(1, 3))  # Pick 1-3 preferred categories
    visited_places = []  # Empty for now, can be updated later with real visited places
    
    return {
        "uid": str(uid),
        "name": name,
        "age": age,
        "preferences": preferences,
        "visited_places": visited_places
    }

# Generate multiple users
def generate_users(count=100):
    users = []
    for uid in range(1, count + 1):
        users.append(generate_user(uid))
    return users

# Upload users to Firestore
def upload_users_to_firestore(users):
    users_ref = db.collection("users")
    for user in users:
        users_ref.document(user["uid"]).set(user)
    print(f"Uploaded {len(users)} users to Firestore successfully!")

if __name__ == "__main__":
    num_users = 500  # Change as needed
    users = generate_users(num_users)
    upload_users_to_firestore(users)
    
    # Save to JSON file as backup
    # with open("synthetic_users.json", "w") as f:
    #     json.dump(users, f, indent=4)
    # print("Synthetic user data saved to synthetic_users.json")
