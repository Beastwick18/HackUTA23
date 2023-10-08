import streamlit as st
import requests
import base64
import json

picture = st.camera_input("Take a picture")

with (open("data.json","r")) as f:
    config = json.load(f)

if picture:
    data ={"image": base64.b64encode(picture.getvalue()), "username": "potato"} 
    r = requests.post("https://hackuta23-8snbt8yuwk7gbtvchfnu7s.streamlit.app/api/upload_image", data)
    
    info = json.loads(r.content)
    ts = ""
    
    for a in info["data"]:
        ts += (f"{a['description']}|")
    
    new = ts.split("|")
    new.pop()
    
    genre = st.radio("Pick an object", new)

next = st.button("Proceed")
if next:
    data = {"id": config["room_id"], "roundItem" : genre}
    r = requests.post("https://hackuta23-8snbt8yuwk7gbtvchfnu7s.streamlit.app/api/set_round_item", data)
    
    