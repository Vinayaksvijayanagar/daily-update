import streamlit as st
#checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("You agreed to the terms and conditions")
else:
    st.write("You did not agree to the terms and conditions")
    
#radio button
gender = st.radio("Select your gender", ("Male", "Female", "Other"))
st.write("You selected:", gender)     

#selectbox
option = st.selectbox("Select your country", ("USA", "Canada", "UK", "Australia"))
st.write("You selected:", option)   

#multiselect
options = st.multiselect("Select your favorite colors", ("Red", "Green", "Blue", "Yellow"))
st.write("You selected:", options)

#slider
age = st.slider("Select your age", 0, 100, 25)  
st.write("Your age is:", age)

#text input
name = st.text_input("Enter your name")         
st.write("Your name is:", name)

#text area
message = st.text_area("Enter your message")        
st.write("Your message is:", message)

#date input
date = st.date_input("Select a date")   
st.write("You selected:", date)

#time input
time = st.time_input("Select a time")       
st.write("You selected:", time)

#file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

#color picker
color = st.color_picker("Pick a color") 
st.write("You picked:", color)

#number input
number = st.number_input("Enter a number", 0,100,50)
st.write("You entered:", number)    

import streamlit as st
#checkbox 
#radio button
#selectbox
#multiselect
#slider
#text input
#text area
#date input
#time input
#file uploader
#color picker
#number input
 
