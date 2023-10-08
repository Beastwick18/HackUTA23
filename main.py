import streamlit as st
import requests
import time 
import json
import base64
import streamlit_book as stb

st.set_page_config(initial_sidebar_state="collapsed")

#Create room
@st.cache_resource
def create_game(image, labels, selected):
    import streamlit as st
    import requests
    import time 
    import json
    import base64
    import streamlit_book as stb
    
    room_id = 0
    data = {"image": image, "labels": labels, "selected" : selected}
    room = requests.post("http://10.183.235.231:3000/api/create_entry",data)
    print(room.content)
    if room.status_code == 200:
        room_id = room.content.decode()
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


picture = st.camera_input("Take a picture")

if picture:
    data ={"image": base64.b64encode(picture.getvalue()), "username": "potato"} 
    r = requests.post("http://10.183.235.231:3000/api/upload_image", data)
    
    info = json.loads(r.content)
    ts = ""
    
    for a in info["data"]:
        ts += (f"{a['description']}|")
    
    new = ts.split("|")
    new.pop()
    
    genre = st.radio("Pick an object", new)
    
    next = st.button("Proceed")
    
    if next:    
        room_id = create_game(base64.b64encode(picture.getvalue()),
                              new,
                              genre)
        i = st.text("Room id: "+ str(room_id))
        st.text("Players: ")
        start = st.button("Start game")
        requests.post("http://10.183.235.231:3000/api/room_start", json={"id" : room_id})
        waiting_loop({"id": room_id}, start)