import firebase_admin
from firebase_admin import credentials, firestore
import os

env_cred = os.getenv("FIREBASE_CREDENTIALS")
cred = credentials.Certificate(env_cred)
firebase_admin.initialize_app(cred)

db = firestore.client()
