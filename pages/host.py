import streamlit as st
import pandas as pd

st.title = st.write("Host")
with st.container():
    col1,col2 = st.columns(2)
    data_df = pd.DataFrame(
    {
        "players": ["player 1", "player 2", "player 3", "player 4", "player 5"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "players": st.column_config.TextColumn(
            "players",
            width="large",
            disabled=True,
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)
st.button("Start the game",type="primary")

st.markdown("""
<style>
    .st-emotion-cache-9aoz2h {
    font-size: 150px;
    margin: auto;
    width: 70%;
    border: 3px;
    padding: 50px;
}
     .element.style {
    display: flex;
    align-items: center;
    justify-content: center;
     }
            
            .st-emotion-cache-1hynsf2 {
    width: 704px;
    position: relative
    }
    
    p, ol, ul, dl {
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 3rem;
    font-weight: 400;
}
            
</style>""", unsafe_allow_html=True)

st.markdown("""
<style>
            
.st-emotion-cache-fg4pbf{
            background: red;
            animation: mymove 20s infinite;
}      
@keyframes mymove {
  0%   { background: #33CCCC; }
  20%  { background: #33CC36; }
  40%  { background: #B8CC33; }
  60%  { background: #FCCA00; }
  80%  { background: #33CC36; }
  100% { background: #33CCCC; }
}

body {
  background: #33CCCC; /* Fallback */
  animation: color 9s infinite linear;
  text-align: center;
  padding: 2em;
}
h1 {
  text-align: center;
  font-family: 'Kavoon', sans-serif;
  font-size: 2.5em;
  color: white;
}
  </style>""", unsafe_allow_html=True)
