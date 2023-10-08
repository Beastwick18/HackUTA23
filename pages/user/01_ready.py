import streamlit as st
import json
import requests

with (open("data.json", "r")) as f:
    config = json.load(f)

data = {"username": config["username"]}
requests.post("http://10.183.235.231:3000/api/update_player",json=data )

    