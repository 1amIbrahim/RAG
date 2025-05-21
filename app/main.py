
import streamlit as st
from .chat import ChatPage
class App():
    def ui(self):
        st.set_page_config(page_title="Doc-Rag",layout="wide")

        st.title("Doc-Rag")
        
        tabs = st.tabs(["Login", "Chat", "Files", "Resources","Settings","Help"])
        
        with tabs[0]:
            st.header("Login")
            st.write("Welcome to the Doc-Rag system.")

        with tabs[1]:
            st.header("Chat")
            ChatPage()

        with tabs[2]:
            st.header("Files")
            st.write("Perform document search here.")

        with tabs[3]:
            st.header("Resources")
            st.write("Configure the application Resources.")
    
        with tabs[4]:
            st.header("Settings")
            st.write("Configure the application Settings.")
        
        with tabs[5]:
            st.header("Help")
            st.write("Help Page.")