import streamlit as st
import requests
import time 
import json
import base64
import streamlit_book as stb


#Create room
@st.cache_resource
def create_game():
    import streamlit as st
    import requests
    import time 
    import json
    import base64
    import streamlit_book as stb
    
    room_id = 0
    room = requests.get("http://10.183.235.231:3000/api/create_entry")
    print(room.content)
    if room.status_code == 200:
        room_id = room.content.decode()
        with open("data.json", "w") as f:
            json.dump({"room_id": room_id},f)
        return room_id
    else:
        print("Error")
        return 0
    
@st.cache_resource
def waiting_loop(data, start):
    import streamlit as st
    import requests
    import time 
    import json
    import base64
    import streamlit_book as stb
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
        if start:
            new_r = requests.post("http://10.183.235.231:3000/api/room_start", json=data)
            break
        time.sleep(1)
    return

    
room_id = create_game()
i = st.text("Room id: "+ str(room_id))
st.text("Players: ")
start = st.button("Start game")
waiting_loop({"id": room_id}, start)