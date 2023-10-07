import streamlit as st
from thegsm import test

st.title("the game")

gaming = st.text_input("give me a number")
button = st.button("request")
r = test(gaming)

label = st.text("")
label.text(r)

