import streamlit as st;
import subprocess;
import os;
import sys;

# Python importing bullshit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "pbl5")))
from pbl5 import ner;

def add_data_block(file_name: str, java_class: str, code: str, diagnosis: str):
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.caption("File")
            st.code(file_name, language="text")
        with col2:
            st.caption("Java Class")
            st.code(java_class, language="java")

        st.caption("Code")
        st.code(code, language="java")

        st.caption("Diagnosis")
        st.info(diagnosis)

def execute(url):
    _, result = ner.run_git(url);
    for path, entry in result:
        add_data_block(
            path,
            entry["Class"],
            entry["Code"],
            "nothing"
        );

st.title("lingang guliguli");

url = st.text_input("link");

if st.button("show shit"):
    if url:
        st.write(f"actual {url} shit");
        execute(url);
    else:
        st.warning("Please enter a link");

