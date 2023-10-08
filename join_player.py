import streamlit as st
import requests

u = st.text_input(" Enter the username")
t = st.text_input(" Enter the room id")
s = st.button("connect")
d = {"username": u, "id": t}
if s:
    r = requests.post("http://10.183.235.231:3000/api/join_player",json=d)
    print(r.content)