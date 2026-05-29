import streamlit as st
import time

#initial header with markdown
st.markdown("<h1>User Registration<h2>", unsafe_allow_html=True)
#creating a form object
form =  st.form("form1")
form.text_input("FIRST NAME")

form.form_submit_button("submit")

with st.form("form2"):
    col1, col2 = st.columns(2)
    col1.text_input("demonstration1")
    col2.text_input("demonstration2")
    st.text_input("First_name")
    st.checkbox("hey")
    st.form_submit_button("submit")

