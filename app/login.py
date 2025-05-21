import streamlit as st
import json
from pathlib import Path
import hashlib

USER_DB_PATH = Path("users.json")

def load_users():
    if USER_DB_PATH.exists():
        with open(USER_DB_PATH, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB_PATH, "w") as f:
        json.dump(users, f, indent=2)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

class LoginPage:
    def __init__(self):
        self.users = load_users()
        self.render()

    def render(self):
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        if "username" not in st.session_state:
            st.session_state.username = None
        if "history" not in st.session_state:
            st.session_state.history = []

        if st.session_state.logged_in:
            self.render_logout()
        else:
            self.render_auth_form()

    def render_auth_form(self):
        tab = st.radio("Choose action", ["Login", "Register"], horizontal=True)

        if tab == "Register":
            self.render_register()
        else:
            self.render_login()

    def render_register(self):
        st.subheader("📝 Create an Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Register"):
            if username in self.users:
                st.error("Username already exists.")
            elif password != confirm:
                st.error("Passwords do not match.")
            elif not username or not password:
                st.error("All fields are required.")
            else:
                self.users[username] = {
                    "password": hash_password(password),
                    "history": [],
                }
                save_users(self.users)
                st.success("Registration successful! Please login.")

    def render_login(self):
        st.subheader("🔑 Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            user = self.users.get(username)
            if not user or hash_password(password) != user["password"]:
                st.error("Invalid username or password.")
            else:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.history = user.get("history", [])
                st.success(f"Welcome back, {username}!")
                st.rerun()

    def render_logout(self):
        st.success(f"✅ Logged in as: `{st.session_state.username}`")
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state.history = []
            st.rerun()
