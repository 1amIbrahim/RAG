import streamlit as st
from .components import render_index_table, render_add_index_form

def render_indices():
    """Main function to render the index management interface"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.subheader("Existing Indices")
        render_index_table()
        st.selectbox("Selected Index ID", [-1], key="selected_index_id")
        st.button("Load Index Details", key="load_index_details")
    
    with col2:
        st.subheader("Add New Index")
        render_add_index_form()