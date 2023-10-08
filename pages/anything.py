import streamlit as st
import streamlit_book as stb

#st.set_page_config(initial_sidebar_state="collapsed")
stb.set_chapter_config(path="pages/anything.py", save_answers=False)

picture = st.camera_input("Take a picture")
if picture:
    print("te goat")
    st.image(picture)
