import streamlit as st


def change():
    print("changed")

st.checkbox("I agree to the terms and conditions")
st.checkbox("chekbox", value=True)#default is false
state = st.checkbox("chekbox")
if state:
    st.write("hi")
else:
    pass

#creating a radio button
radio_button = st.radio("well what is you name", options = ("Alice", "Bob", "Charlie"))
#print(radio_button)
#defining a button

def btn_click():
    print("it good to learn steamlit")

st.button("click me", on_click=btn_click)
select = st.selectbox("what isnyour favorite color", options = ("red", "blue", "green"))

print(select)

multiselect =  st.multiselect("what are your favorite colors", 
                              options = ("red", "blue", "green", "yellow"))
st.write(multiselect)