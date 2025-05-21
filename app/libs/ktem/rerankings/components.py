import streamlit as st

def render_reranking_table():
    """Render the table of existing reranking models"""
    st.dataframe({
        "Name": ["cohere"],
        "Vendor": ["CohereReranking"],
        "Default": [""]
    }, use_container_width=True)

def render_add_reranking_form():
    """Render the form to add new reranking models"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Model Name", key="new_reranking_name")
        st.selectbox("Vendor", ["Cohere", "Other"], key="reranking_vendor")
    
    with col2:
        st.text_input("API Key", type="password", key="reranking_api_key")
        st.number_input("Timeout (seconds)", min_value=1, value=30, key="reranking_timeout")
    
    st.button("Add Reranking Model", key="add_reranking")