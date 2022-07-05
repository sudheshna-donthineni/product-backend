import firebase_admin
from firebase_admin import credentials, firestore
import os

cred = credentials.Certificate(
    {
        "type": "service_account",
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "token_uri": "https://oauth2.googleapis.com/token",
    }
)
firebase_admin.initialize_app(cred)
db = firestore.client()
