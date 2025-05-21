import streamlit as st
from .components import render_reranking_table, render_add_reranking_form

def render_rerankings():
    """Main function to render the reranking management interface"""
    st.subheader("Reranking Models")
    
    # Display existing reranking models
    render_reranking_table()
    
    # Add new reranking form
    with st.expander("Add New Reranking Model"):
        render_add_reranking_form()