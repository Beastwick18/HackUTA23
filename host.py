import streamlit as st
import requests
import time 
import json

room_id = 0

#Create room
def create_room():
    r = requests.get("http://10.183.235.231:3000/api/create_entry")
    print(r.content)
    if r.status_code == 200:
        global room_id
        room_id = r.content.decode()
    else:
        print("Error")
    
#Wait for players
create_room()
data = {"id": room_id}
i = st.text("Room id: "+room_id)
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
        new_r = requests.post("http://10.183.235.231:3000/api/room_status", json=data)
        break
    time.sleep(1)
    

    