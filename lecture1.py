import streamlit as st
import time

#initial header with markdown
st.markdown("<h1 style='text-align: center;'>User Registration</h1>", unsafe_allow_html=True)
#creating a form object
form =  st.form("form1")
form.text_input("FIRST NAME")

form.form_submit_button("submit")

with st.form("form2", clear_on_submit=True):
    day, month, year = st.columns(3)
    
    c = day.text_input("DAY")
    a = month.text_input("MONTH")
    b = year.text_input("year")
    
    sub = st.form_submit_button("submit")
    if sub :
        if c =="" or a == "" or b == "" :
            st.warning("please fil the empty widgets")
    
        else: st.success("from submitted") 
    #     st.write("please fill and submit the form")
    # else:
    #         st.write(a)
    #         st.write(b)
    #         st.write(c)
    