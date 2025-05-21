import streamlit as st

class FilePage:
    def __init__(self):
        self.render()

    def upload_file_ui(self):
        pass

    def use_web_links_ui(self):
        pass

    def advanced_indexing_options_ui(self):
        pass

    def file_list_ui(self):
        pass

    def file_details_ui(self):
        pass

    def render(self):
        st.title("Files")

        tabs = st.tabs(["File Collection", "GraphRAG Collection", "LightRAG Collection"])

        with tabs[0]:
            file_tabs = st.tabs(["Upload Files", "Use Web Links"])

            with file_tabs[0]:
                st.markdown("### Upload Files")
                st.markdown("""
                Drop File Here  
                or  
                Click to Upload
                """)
                st.markdown("""
                - Supported file types: .png, .jpeg, .jpg, .tiff, .tif, .pdf, .xls, .xlsx, .doc, .docx, .pptx, .csv, .html, .mhtml, .txt, .md, .zip  
                - Maximum file size: 1000 MB
                """)
                self.upload_file_ui()

            with file_tabs[1]:
                st.markdown("### Use Web Links")
                self.use_web_links_ui()

            st.divider()
            st.markdown("### Files")
            st.text_input("Filter by name:", help="(1) Case-insensitive. (2) Search with empty string to show all files.")

            st.markdown("#### File Table")
            st.dataframe({
                "name": ["-"], 
                "size": ["-"], 
                "token": ["-"], 
                "loader": ["-"], 
                "date_created": ["-"]
            })

            self.file_list_ui()
            self.file_details_ui()

            with st.expander("Advance options"):
                self.advanced_indexing_options_ui()

            st.button("Upload and Index")
