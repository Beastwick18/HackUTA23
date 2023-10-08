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
i = st.text("Room id: "+room_id)
st.text("Players: ")
c = st.container()
while(True):
    r = requests.get("http://10.183.235.231:3000/api/room_info")
    j = json.loads(r.content)
    for a in j["data"]:
        c.add_rows(a)
    time.sleep(1)
    c = st.empty()
    