import streamlit as st

def render_embeddings():
    st.subheader("Embedding Models")
    st.dataframe({
        "Name": ["openai", "cohere", "google", "mistral"],
        "Vendor": ["OpenAIEmbeddings", "LCCohereEmbeddings", "LCGoogleEmbeddings", "LCMistralEmbeddings"],
        "Default": ["", "", "", ""]
    }, use_container_width=True)
    
    st.button("Add New Embedding", key="add_embedding")