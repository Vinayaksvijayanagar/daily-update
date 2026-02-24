#form 
import streamlit as st
with st.form("user form"):
    name = st.text_input("enter name")
    age = st.number_input("enter age",min_value = 0)
    a= st.form_submit_button("click")
if a :
    st.write(f"your name:{name} and age is:{age}")
#. Layout & Columns
col1,col2 = st.columns(2)
with col1:
    a = st.text_input("enter col1")
    st.write(a)
with col2:
    b = st.text_input("enter col2")
    st.write(b)
    
#Sidebar
st.title("setting")
b = st.sidebar.selectbox("Select Model", ["Linear", "Random Forest"])

#Displaying Data Properly
df = [1,2,3,4]
st.dataframe(df)

#Upload File → Read with Pandas
file = st.file_uploader("upload file")
if file:
    import pandas as pd
    data = pd.read_csv(file)
    st.dataframe(data.head())