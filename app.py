import streamlit as st
import gmail
import github

st.set_page_config(page_title="Login Page", layout="centered")

# Initialize session state
if "login_choice" not in st.session_state:
    st.session_state.login_choice = None

# Add custom CSS styling
st.markdown("""
    <style>
    .login-btn {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
        cursor: pointer;
        border: none;
    }
    .login-btn:hover {
        transform: scale(1.05);
    }
    .login-img {
        width: 80px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🔐 Login Page</h1>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

# Show Gmail button if GitHub isn't selected
with col1:
    if st.session_state.login_choice is None or st.session_state.login_choice == "gmail":
        if st.button("Click", key="gmail"):
            st.session_state.login_choice = "gmail"
            gmail.main()
        st.markdown(f"""
        <div class="login-btn">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="login-img"/>
            <span>Login with Gmail</span>
        </div>
        """, unsafe_allow_html=True)

# Show GitHub button if Gmail isn't selected
with col2:
    if st.session_state.login_choice is None or st.session_state.login_choice == "github":
        if st.button("Click", key="github"):
            st.session_state.login_choice = "github"
            github.main()
        st.markdown(f"""
        <div class="login-btn">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" class="login-img"/>
            <span>Login with GitHub</span>
        </div>
        """, unsafe_allow_html=True)
