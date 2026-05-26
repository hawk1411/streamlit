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
st.title("hi! i am stramlit web")
st.subheader("hi! i am your sun header")
st.header("i am header")
st.text("hi i am text function and programmers use me in place of paragraph")
st.markdown("[GOOGLE](https://www.google.com/)")
st.markdown("---")
st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}") #raw string is denoted by 
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("hello world")
def func():
return 0; """
st.code(code,language = "python")
st.write("# ill explore it tommorow")
st.metric(label="wind speed", value="120m\^-1", delta='-1.4ms\^-1')#i will see this tommorow th workong of m/s thing
st.table(tabel)
st.dataframe(tabel)
st.image("image.png", caption="this is a image",width=90)
#st.audio("audio.mp3")
#st.video("video.mp4")

