import streamlit as st
from thegsm import test
import requests

st.title("the game")

gaming = st.text_input("give me a number")
button = st.button("request")
r = test(gaming)

label = st.text("")
label.text(r)

def test(id):
    data = {"id" : id}
    r = requests.post("http://10.183.235.231:3000/api/post_test",json=data)
    
    return r.content