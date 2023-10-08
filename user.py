import streamlit as st
import requests
import time 
import json

room_id = 0

u = st.text_input(" Enter the username")
t = st.text_input(" Enter the room id")
s = st.button("connect")
d = {"username": u, "id": t}
room_id = t
data = {"id" : room_id}

if s:
    r = requests.post("http://10.183.235.231:3000/api/join_player",json=d)
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
            r = requests.get("http://10.183.235.231:3000/api/room_info", json=data)
            j = json.loads(r.content)
            long = ""
            for a in j["data"]:
                long+=a["username"]
            if long != long_before:
                c.empty()
                d = c.container()
                with d.container():
                    for strr in j["data"]:                                  
                        d.write(strr["username"])
            new_r = requests.get("http://10.183.235.231:3000/api/room_status", json=data)
            if new_r.content.decode() == 1:
                break
            time.sleep(1)
        
            
