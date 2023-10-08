import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
<style>
            
.st-emotion-cache-fg4pbf{
            background: red;
            animation: mymove 20s infinite;
}      
@keyframes mymove {
  0%   { background: #33CCCC; }
  20%  { background: #33CC36; }
  40%  { background: #B8CC33; }
  60%  { background: #FCCA00; }
  80%  { background: #33CC36; }
  100% { background: #33CCCC; }
}

body {
  background: #33CCCC; /* Fallback */
  animation: color 9s infinite linear;
  text-align: center;
  padding: 2em;
}
h1 {
  text-align: center;
  font-family: 'Kavoon', sans-serif;
  font-size: 2.5em;
  color: white;
}
  </style>""", unsafe_allow_html=True)

with st.container():
    
    st.text_input("Username",key="placeholder1")
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


