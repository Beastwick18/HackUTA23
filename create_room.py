import streamlit as st
import requests

b = st.button("create room")
if b:
    #w = requests.post("http://10.183.235.231:3000/api/create_entry")
    r = requests.get("http://10.183.235.231:3000/api/create_entry")
    st.text(r.content)