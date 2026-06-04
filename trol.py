import streamlit as st;
import subprocess;
import os;

def execute(url) -> str:
    orig_dir = os.getcwd();
    ner_path = "/mnt/d/pbl5-queries/";

    try:
        os.chdir(ner_path);
        result = subprocess.run(
            ["uv", "run", "ner.py", "-r", url],
            capture_output=True,
            text=True,
            check=True,
        );

        with open("csv.csv", "r") as file:
            return file.read();
    finally:
        os.chdir(orig_dir);

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

st.title("lingang guliguli");

url = st.text_input("link");

mock_data = [
    {
        "file": "UserController.java",
        "class": "UserController",
        "code": "public void login() {\n    log.info(\"User logging in\");\n}",
        "diagnosis": "lingang guliguliguli"
    },
    {
        "file": "AuthService.java",
        "class": "AuthService",
        "code": "if (password == \"123\") {\n    grantAccess();\n}",
        "diagnosis": "lingang guliguliguli"
    }
]

if st.button("show shit"):
    if url:
        st.write(f"actual {url} shit");
        for item in mock_data:
            add_data_block(item["file"], item["class"], item["code"], item["diagnosis"]);

        st.write(execute(url));
    else:
        st.warning("Please enter a link");

