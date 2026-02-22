import streamlit as st

st.header("Buttons")

if st.button("Click me"):
    st.write("button clicked")
else:
    st.write("button not clicked")