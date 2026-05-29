import streamlit as st;

st.title("lingang guliguli");

url = st.text_input("link");

if st.checkbox("show shit"):
    st.write(f"actual {url} shit");

