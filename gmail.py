import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from urllib.parse import urlencode
import os

# Set your credentials from Google Cloud Console
CLIENT_ID = "replace you id"
CLIENT_SECRET = "replace you secret"
REDIRECT_URI = "http://localhost:8501"

# Google OAuth URLs
AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
USERINFO_ENDPOINT = "https://www.googleapis.com/oauth2/v3/userinfo"

# Create OAuth session
def create_oauth_session():
    return OAuth2Session(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="openid email profile",
    )

# Main app
def main():
    st.title("🔐 Gmail Login with Streamlit")

    query_params = st.query_params

    if "code" not in query_params:
        # Not logged in
        oauth = create_oauth_session()
        auth_url, _ = oauth.create_authorization_url(AUTHORIZATION_ENDPOINT)
        st.write("Please login using your Gmail account:")
        st.markdown(f"[Login with Google]({auth_url})")
    else:
        # User redirected back with code
        code = query_params["code"]
        oauth = create_oauth_session()

        token = oauth.fetch_token(
            TOKEN_ENDPOINT,
            code=code,
        )

        # Get user info
        resp = oauth.get(USERINFO_ENDPOINT)
        user_info = resp.json()

        st.success("✅ Login Successful!")
        st.write("Welcome,", user_info["name"])
        
        st.write("Email:", user_info["email"])


