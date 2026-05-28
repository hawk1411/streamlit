import streamlit as st


def change():
    print("hello i am being called by slider")

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
st.write(select)

multiselect =  st.multiselect("what are your favorite colors", 
                              options = ("red", "blue", "green", "yellow"))
st.write(multiselect)
images = st.file_uploader("upload your image", type = ["jpg", "png"],accept_multiple_files = True,)

# if image is not None:
#     st.image(image)#st.video,st.audio
if images is not None:
    for image in images:
        st.image(image)
        
st.slider("this is a slider")#kind of refreshes the page totally
val = st.slider("this is a slidr",min_value=0, max_value=50, value=50, step=5,on_change=change)
print(val)    

#multiple file uploader
st.file_uploader("upload your file", type = ["pdf", "docx"], accept_multiple_files = True)

name = st.text_input("enter your name")
st.write(name)
print(name)
text  = st.text_area("enter your address")
print(text)
sde = st.date_input("enter your date of birth")
st.write(sde)
opy = st.select_slider("what is your favorite color", options = ("blue", "green", "yellow"))
st.write(opy)