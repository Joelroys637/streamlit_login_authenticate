import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from urllib.parse import urlencode
# Replace with your GitHub OAuth credentials
GITHUB_CLIENT_ID = "replace you id"
GITHUB_CLIENT_SECRET = "replace you secret key"
REDIRECT_URI = "http://localhost:8501"

# OAuth endpoints for GitHub
AUTHORIZATION_ENDPOINT = "https://github.com/login/oauth/authorize"
TOKEN_ENDPOINT = "https://github.com/login/oauth/access_token"
USERINFO_ENDPOINT = "https://api.github.com/user"

def create_oauth_session():
    return OAuth2Session(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="read:user user:email",
    )

def main():
    st.title("🔐 GitHub Login with Streamlit")

    query_params = st.query_params

    if "code" not in query_params:
        oauth = create_oauth_session()
        auth_url, _ = oauth.create_authorization_url(AUTHORIZATION_ENDPOINT)
        st.markdown(f"[Login with GitHub]({auth_url})")
    else:
        code = query_params["code"]
        oauth = create_oauth_session()
        token = oauth.fetch_token(
            TOKEN_ENDPOINT,
            code=code,
            authorization_response=REDIRECT_URI + "?" + urlencode(st.query_params),
            include_client_id=True,
        )

        # Get user info
        resp = oauth.get(USERINFO_ENDPOINT)
        user_info = resp.json()

        st.success("✅ GitHub Login Successful!")
        st.write("👤 Username:", user_info.get("login"))
        st.write("📧 Email:", user_info.get("email"))
        st.image(user_info.get("avatar_url"))
