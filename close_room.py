import streamlit as st
import requests

t= st.text_area("Insert the id of the room")
s= st.button("Click to close the room")
id = {"id": t}
if s:
    r = requests.post("http://10.183.235.231:3000/api/close_room",json=id)
    print(r.content)
