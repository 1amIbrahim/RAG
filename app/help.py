import streamlit as st
from pathlib import Path

class HelpPage:
    def __init__(self):
        self.doc_dir = Path("docs")  # Directory for local markdown files (optional)
        self.render()

    def render(self):
        st.title("📘 Help & Documentation")

        # About Section
        with st.expander("About", expanded=True):
            st.markdown(self.get_about_content())

        # User Guide Section
        with st.expander("User Guide"):
            st.markdown(self.get_user_guide_content())

        # FAQ Section
        with st.expander("FAQ"):
            st.markdown(self.get_faq_content())

        # Contact / Feedback Section
        with st.expander("Contact / Feedback"):
            st.markdown(self.get_contact_content())

    def get_about_content(self):
        return """
### About This App

This application provides an interactive interface for users to [insert purpose here].

- Version: `1.0.0`
- Last Updated: `May 2025`

Developed with ❤️ using [Streamlit](https://streamlit.io).
"""

    def get_user_guide_content(self):
        return """
### User Guide

**Getting Started**
1. Open the app.
2. Navigate using the sidebar.
3. Start interacting with the features.

**Tips**
- Use the top menu for quick actions.
- You can refresh the app anytime with `Ctrl + R`.

"""

    def get_faq_content(self):
        return """
### Frequently Asked Questions

**Q: How do I reset the app?**  
A: Click the 'Rerun' button in the top-right.

**Q: Can I use this app offline?**  
A: No, it requires an internet connection to load some data.

**Q: Who do I contact for support?**  
A: See the Contact section below.
"""

    def get_contact_content(self):
        return """
### Contact / Feedback

For questions, feature requests, or issues, please contact us at:

📧 Email: [support@example.com](mailto:support@example.com)  
🐞 GitHub: [github.com/your-repo](https://github.com/your-repo)
"""

# Example usage
if __name__ == "__main__":
    HelpPage()
