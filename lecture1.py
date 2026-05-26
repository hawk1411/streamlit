import streamlit as st
import pandas as pd
tabel = pd.DataFrame({"column 1":[1,2,3,4,5,6,7], "column 2": [11,12,13,14,15,16,17]})
st.markdown("""
            <style>
            .stAppDeployButton{ 
                visibility: hidden;
            } 
            </style>
            """, unsafe_allow_html=True)

def change():
    print("changed")
    print(st.session_state.changed)#using key we may track the seeion

state = st.checkbox("basic chcekbox",value=False, on_change=change, key="changed")

if state:
    st.write("chek box was ticked")
else:
    pass #no need to do anything

#invoking of a function using this chek box

