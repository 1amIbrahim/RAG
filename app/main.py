import streamlit as st
from .chat import ChatPage
from .help import HelpPage
from .files import FilePage
from .login import LoginPage  # <- add this if it's in a separate file
from .libs.ktem.pages.resources import render_resources
class App():
    
    def ui(self):
        st.set_page_config(page_title="Doc-RAG", layout="wide")
        st.title("📄 Doc-RAG")

        # Initialize session state
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        if "username" not in st.session_state:
            st.session_state.username = None

        tabs = st.tabs(["Login", "Chat", "Files", "Resources", "Settings", "Help"])

        # LOGIN TAB
        with tabs[0]:
            st.header("🔐 Login")
            LoginPage()

        # AUTHENTICATED TABS
        if st.session_state.logged_in:
            with tabs[1]:
                ChatPage()

            with tabs[2]:
                st.header("📁 Files")
                st.write("Perform document search here.")

            with tabs[3]:
                st.header("🔧 Resources")
                render_resources()

            with tabs[4]:
                st.header("⚙️ Settings")
                st.write("Configure application settings.")

        else:
            for i in range(1, 5):
                with tabs[i]:
                    st.warning("🔒 Please log in to access this section.")

        # HELP TAB (always accessible)
        with tabs[5]:
            st.header("❓ Help")
            HelpPage()
