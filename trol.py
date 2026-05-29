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

st.title("lingang guliguli");

url = st.text_input("link");

if st.checkbox("show shit"):
    st.write(f"actual {url} shit");
    st.write(execute(url));

