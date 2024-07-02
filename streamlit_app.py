''' import streamlit as st
import firebase_admin
from firebase_admin import credentials, storage
from io import BytesIO
import os

# Initialize Firebase
def initialize_firebase():
    key_path = "firestore-key.json"  # Update this path as needed
    if not os.path.isfile(key_path):
        st.error(f"Service account key file not found at path: {key_path}")
        return

    if not firebase_admin._apps:
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'thin-film-database.appspot.com'
        })
        st.success("Firebase initialized successfully.")

# Upload file to Firebase Storage
def upload_to_firebase(file, file_name):
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_file(file)
    blob.make_public()
    return blob.public_url

# Streamlit app
def main():
    st.title("Text File Upload to Firebase Storage")

    uploaded_file = st.file_uploader("Choose a text file", type=["txt", "md", "csv"])

    if uploaded_file is not None:
        file_name = uploaded_file.name
        file = BytesIO(uploaded_file.read())

        # Display file content
        st.text(f"File content: {file.getvalue().decode('utf-8')}")

        if st.button("Upload to Firebase"):
            initialize_firebase()
            if firebase_admin._apps:

                public_url = upload_to_firebase(file, file_name)
                st.success(f"File uploaded successfully! [View File]({public_url})")'''

import pyrebase
import streamlit as st

config = {
  "apiKey": "AIzaSyDf_Gf0N4G2DygyRXid4XBdu9k5q4ITK3k",
  "authDomain": "thin-film-database.firebaseapp.com",
  "projectId": "thin-film-database",
  "storageBucket": "thin-film-database.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase_storage = pyrebase.initilize_app(config)
storage = firebase_storage.storage()

uploaded_file = st.file_uploader("Choose a file", type=["txt", "md", "csv"])

storage.child(uploaded_file).put("data")







