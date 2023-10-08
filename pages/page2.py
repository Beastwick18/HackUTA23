import streamlit as st
with st.container():
    st.title("Object")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
with st.container():
    picture = st.camera_input("take a picture")
    if picture:
        st.image(picture)
    