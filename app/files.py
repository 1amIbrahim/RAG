import streamlit as st

def upload_file_ui():
    pass

def use_web_links_ui():
    pass

def advanced_indexing_options_ui():
    pass

def file_list_ui():
    pass

def file_details_ui():
    pass

def ui():
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
            upload_file_ui()

        with file_tabs[1]:
            st.markdown("### Use Web Links")
            use_web_links_ui()

    with tabs[0]:
        st.divider()
        st.markdown("### Files")
        st.text_input("Filter by name:", help="(1) Case-insensitive. (2) Search with empty string to show all files.")

        st.markdown("#### File Table")
        st.dataframe({"name": ["-"], "size": ["-"], "token": ["-"], "loader": ["-"], "date_created": ["-"]})

        file_list_ui()
        file_details_ui()

        with st.expander("Advance options"):
            advanced_indexing_options_ui()

        st.button("Upload and Index")
 