import streamlit as st
import requests
import time 
import json
import base64

st.markdown("""
<style>
        .wrapperclass{
  </style>""", unsafe_allow_html=True)


room_id = 0

con = st.empty()

with con.container():
    u = st.text_input(" Enter the username")
    t = st.text_input(" Enter the room id")
    s = st.button("connect")
    d = {"username": u, "id": t}
    room_id = t
    data = {"id" : room_id}

    if s:
        r = requests.post("https://focus-sequencer-401321.uc.r.appspot.com/api/join_player",json=d)
        if r.status_code == 200:
            u = st.empty()
            t = st.empty()
            s = st.empty()
            st.text("Players: ")
            c = st.empty()
            long = ""
            long_before = ""
            while(True):
                long_before = long
                r = requests.get("https://focus-sequencer-401321.uc.r.appspot.com/api/room_info", json=data)
                j = json.loads(r.content)["data"]
                long = ""
                for a in j["data"]:
                    long+=a["username"]
                time.sleep(1)
                if long != long_before:
                    c.empty()
                    d = c.container()
                    with d.container():
                        for strr in j["data"]:                                  
                            d.write(strr["username"])
                new_r = requests.get("https://focus-sequencer-401321.uc.r.appspot.com/api/room_status", json=data)
                if int(new_r.content.decode()) == 1:
                    break
try:        
    response = requests.post("https://focus-sequencer-401321.uc.r.appspot.com/api/entry_info", json={"id":room_id})
    result = json.loads(response.content)["data"]
    st.image(base64.b64decode(result["image"]))
    genre = st.radio("Pick an object", result["labels"])
    next = st.button("Select")
    if next:
        if genre == result["selected"]:
            st.text("winner")
            st.markdown("""
                        <style>
                            .stApp {
                                background-color: #008000;
                            }
                        <style/>
                        """,unsafe_allow_html=True)
        else:
            st.text("Loser")
            st.markdown("""
            <style>
                .stApp {
                    background-color: #ff0000;
                }
            <style/>
            """,unsafe_allow_html=True)
except:
    pass

