import streamlit as st
#checkbox
if st.checkbox("you clicked"):
    st.write("you clicked")
else:
    st.write("try to click")
    
#radio button
gender = st.radio("choose the gende",("male","Female","none"))
st.write("you selected",gender)
#selectbox
nation  = st.selectbox("choose nation",("india","AUS","japan"))  
st.write("your nation is",nation)
#multiselect
language = st.multiselect("choose lanaguage",("Kan","Hindi","Tamil"))
st.write("you choosed language",language)
#slider
range = st.slider("select age range",0,100,25)
st.write("your age is",range)
 

#text input
text = st.text_input("enter the name")
if text:
    st.write("you texted",text)
else:
    pass

#text area
areatext = st.text_area("enter summery")
if areatext:
    st.write("your area",areatext)
else:
    pass
#date input
date = st.date_input("enter date")
st.write(date)

#time input
time = st.time_input("Enter time")
st.write(time) 

#file uploader
file_upload = st.file_uploader("upload file")
if file_upload == None:
     st.write("no file uploaded")
else:
    st.write("uploaded succesfully")

#color picker
color = st.color_picker("select color")
st.write(color)

#number input
 
number = st.number_input("enter number")
st.write(number)

