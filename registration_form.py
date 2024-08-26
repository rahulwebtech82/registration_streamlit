import streamlit as st

st.title("Student Registration Form")
st.subheader("Fill Student All Carrect Details")

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter Your Father name : ")
mobile_no= st.text_input("Enter your mobile number:")
email_id = st.text_input("Enter Your Email Id:")
roll_no = st.text_input("Enter Your Roll number:")
add = st.text_area("Enter Your address: ")
st.success("Select Gender")
gender=st.radio("Choose Gender",("Male","Female"))

import datetime
st.success("Select Your Date Of Birth")
dateofbirth= st.date_input("Today  is" ,datetime.datetime.now())
st.success("Select Your Age")
age = st.slider("What is your Age",1,50)
st.success("Occuption")
occuption= st.multiselect("Choose Your Occuption", ['Engineer', 'Doctor','Teacher','Programmer','Telor'])

button=st.button("Submit")

if button:
    st.code(f"""
                Your Name = {name}\n
                Father Name = {fname}\n
                Mobile Number = {mobile_no}\n
                Email ID = {email_id}\n
                Roll No = {roll_no}\n
                Address = {add}\n
                Gender = {gender}\n
                Date Of Birth = {dateofbirth}\n
                Age = {age}\n
                Occuption= {occuption}\n
     """   
    )
    

    