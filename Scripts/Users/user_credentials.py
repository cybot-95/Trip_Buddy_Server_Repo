#This code fetches the users from the Users table in the database and creates a new collection with uid & password (User Credentials) with default password set to "Login@123"

import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("../../Key/Firebase_key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Default password
default_password = "Login@123"

# Fetch all users from Firestore
def fetch_users():
    users_ref = db.collection("users")
    users = users_ref.stream()
    return [user.to_dict() for user in users]

# Store user credentials
def create_user_credentials():
    users = fetch_users()
    credentials_ref = db.collection("user_credentials")
    
    for user in users:
        uid = user.get("uid")  # Ensure 'uid' exists
        if not uid:
            print(f"Skipping user without UID: {user}")
            continue
        
        # Set credentials in Firestore
        credentials_ref.document(str(uid)).set({
            "uid": uid,
            "password": default_password  # Store plaintext for now (not secure in production!)
        })
        print(f"Credentials created for UID: {uid}")

if __name__ == "__main__":
    create_user_credentials()
    print("User credentials setup complete!")
