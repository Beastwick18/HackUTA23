import streamlit as st
import requests
import base64
import json

picture = st.camera_input("Take a picture")

if picture:
    #r = requests.post("https://focus-sequencer-401321.uc.r.appspot.com/api/upload_image",picture.getvalue())
    data = base64.b64encode(picture.getvalue())
    r = requests.post("http://10.183.235.231:3000/api/upload_image", data)
    
    info = json.loads(r.content)
    ts = ""
    
    for a in info["data"]:
        ts += (f"{a['description']} {a['score']}\n")
    
    st.text(ts)
    