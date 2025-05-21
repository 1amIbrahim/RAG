import streamlit as st
from .user import render_users
from .user_st import render_user_settings

def render_resources():
    st.header("Resources Management")
    
    tabs = st.tabs(["Index Collections", "LLMs", "Embeddings", "Rerankings", "Users"])
    
    with tabs[0]:
        from app.libs.ktem.index import render_indices
        render_indices()
    
    with tabs[1]:
        from app.libs.ktem.llms import render_llms
        render_llms()
    
    with tabs[2]:
        from app.libs.ktem.embeddings import render_embeddings
        render_embeddings()
    
    with tabs[3]:
        from app.libs.ktem.rerankings import render_rerankings
        render_rerankings()
    
    with tabs[4]:
        render_users()