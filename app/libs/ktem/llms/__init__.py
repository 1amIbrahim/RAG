import streamlit as st

def render_llms():
    st.subheader("LLM Management")
    st.dataframe({
        "Name": ["openai", "claude", "google", "groq", "cohere", "mistral"],
        "Vendor": ["ChatOpenAI", "LCAnthropicChat", "LCGeminiChat", "ChatOpenAI", "LCCohereChat", "ChatOpenAI"],
        "Default": ["", "", "✓", "", "", ""]
    }, use_container_width=True)
    
    st.button("Add New LLM", key="add_llm")