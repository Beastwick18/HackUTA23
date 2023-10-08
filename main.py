import streamlit as st
import streamlit_book as stb

st.set_page_config()
stb.set_chapter_config(path="pages/", save_answers=False)

st.button("Client")
st.button("Host")