import streamlit as st

def show_settings():
        st.title("🔧 Kateonmon Settings")

        # === User Settings ===
        with st.expander("👤 User Settings", expanded=False):
            user_profile = st.selectbox(
                "Select User Profile",
                ["Default", "Power User", "Minimal", "Custom"]
            )
            theme_choice = st.selectbox(
                "Choose Theme",
                ["Light", "Dark", "System"]
            )
            notifications = st.radio(
                "Enable Notifications",
                ["Yes", "No"]
            )

        # === Retrieval Settings ===
        with st.expander("📄 Retrieval Settings", expanded=False):
            retrieval_method = st.selectbox(
                "Retrieval Method",
                ["BM25", "Dense Vector", "Hybrid", "Custom"]
            )
            top_k = st.slider("Top-K Results", min_value=1, max_value=100, value=10)
            use_cache = st.checkbox("Enable Retrieval Caching", value=True)

        # === Reasoning Settings ===
        with st.expander("🧠 Reasoning Settings", expanded=False):
            reasoning_mode = st.selectbox(
                "Reasoning Strategy",
                ["Chain of Thought", "Direct Answering", "Step-by-Step"]
            )
            temperature = st.slider("Model Temperature", 0.0, 1.0, 0.7)
            max_tokens = st.number_input("Max Tokens", min_value=50, max_value=4096, value=512, step=50)
