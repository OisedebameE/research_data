import streamlit as st
import firebase_admin
from firebase_admin import credentials, storage
from io import BytesIO

# Initialize Firebase
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("path/to/serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'thin-film-database.appspot.com'
        })

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
            public_url = upload_to_firebase(file, file_name)
            st.success(f"File uploaded successfully! [View File]({public_url})")

if __name__ == "__main__":
    main()
