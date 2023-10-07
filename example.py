import streamlit as st
with st.container():
    st.text_input("Username",key="placeholder1")
    st.text_input("Enter game code here",key="placeholder2")
    st.empty()
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")

col1,col2,col3,col4 = st.columns(4)

col1.button("Host game", type="primary")

col4.button("Join a a game",type="primary")
