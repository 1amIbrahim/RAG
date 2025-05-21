import streamlit as st
from app.libs.ktem.pages.resources import render_resources

class KotaemonApp:
    def run(self):
        st.set_page_config(page_title="Doc-RAG", layout="wide")
        
        # Sidebar navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.radio(
            "Go to",
            ["Chat", "Resources", "Help"]
        )
        
        # Main content area
        if page == "Resources":
            render_resources()