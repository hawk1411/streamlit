import streamlit as st


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