import streamlit as st
import requests
import time 
import json

#Create room
@st.cache_resource
def create_game():
    room_id = 0
    room = requests.get("http://10.183.235.231:3000/api/create_entry")
    print(room.content)
    if room.status_code == 200:
        room_id = room.content.decode()
        return room_id
    else:
        print("Error")
        return 0

#Wait for players
room_id = create_game()
i = st.text("Room id: "+ str(room_id))
data = {"id": room_id}
st.text("Players: ")
c = st.empty()
long = ""
long_before = ""
start = st.button("Start game")
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
    if start:
        new_r = requests.post("http://10.183.235.231:3000/api/room_start", json=data)
        break
    time.sleep(1)
        