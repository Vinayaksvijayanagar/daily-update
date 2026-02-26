import streamlit as st
#form 
with st.form("enter form details"):
    name = st.text_input("enter name")
    age = st.number_input("enter age",min_value = 0)
    a= st.form_submit_button("click")
    if st.form:    
        st.write(f"your name is {name},and age is {age}")
    else:
        st.write("Enter details")
#. Layout & Columns
col1,col2 = st.columns(2)
with col1:
     a = st.text_input("age")
     st.write(a)
with col2:
    b = st.date_input("date")
    st.write(b)
#Sidebar
st.sidebar.selectbox("settings",("A","B"))
if st.sidebar.selectbox == "A":
    st.write("Selected A")
else:
    st.write("Selected B")
    
#Displaying Data Properly
data = [1,2,3,4]
st.dataframe(data)
st.write(data[1])

#Upload File → Read with Pandas
file = st.file_uploader("upload file",type=["xlsx"])
if file:
    import pandas as pd
    data = pd.read_excel(file)
    st.dataframe(data.head())