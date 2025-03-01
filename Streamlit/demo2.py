import streamlit as st
import pandas as pd

email = st.text_input("Enter email")
password = st.text_input("Enter password")
gender = st.selectbox('Select Gender', ['male','female','lesbian','gay'])

btn = st.button('Login karo')

#If button is pressed:
if btn:
    if email == 'vk@gmail.com' and password == '1234':
        st.success("Logged In")
        st.write(gender)
    else:
        st.error("Login Failed")
        
#------------------------------#
#File uploader:

file = st.file_uploader("Upload a csv file")

if file is not None:
    df = pd.read_csv(file) 
    st.dataframe(df.describe())