import streamlit as st
import time
from datetime import time as dt_time
# bar  = st.progress(0,text="Loading...")#strting from 0 its in terms of percentage and the bar is from 1 to 100 initializing value is 0
# for i in range(10):
#     time.sleep(1) #sleep for 1 second
#     bar.progress((i+1)*10)

def converter(value):#(00.00.00)
    m, s, ms = value.split(":")#will split and allocate the values as well
    ts = int(m)*60 + int(s) + int(ms)/1000 #converting the time to seconds
    return ts
# Creating the time input widget with a default value
# Format: hours, minutes, seconds
val =st.time_input("Set an alarm", value = dt_time(0, 0, 0)) #To build the timer, the instructor uses st.time_input. He explains that to set a default value of "00:00:00", you must use a datetime object, not a string or integer
if str(val) != "00:00:00": #if the value is not equal to 00:00:00 then only the timer will start
    sec = converter(str(val))
    per = sec/100#divided into 100 parts
    bar = st.progress(0,text="Loading...")#strting from 0 its in terms of percentage and the bar is from 1 to 100 initializing value is 0
    progress_status = st.empty() #to display the progress status//special object for beep
    for i in range(100):
       
       #when the 100th part of the second willl reach the progress bar will reach the 100 as well
        bar.progress(i+1)
        progress_status.write(f"Progress: {i+1}%")
        time.sleep(per)
else:
    st.write("please select a time")
        
