import streamlit as st

def render_index_table():
    """Render the table of existing indices"""
    st.dataframe({
        "ID": [0],
        "Name": ["-"],
        "Index Type": ["-"]
    }, use_container_width=True)

def render_add_index_form():
    """Render the form to add new indices"""
    st.text_input("Index Name", key="new_index_name")
    st.selectbox("Index Type", ["No options available"], key="index_type")
    st.text_area("Specification (YAML format)", key="index_spec")
    st.button("Add Index", key="add_index")