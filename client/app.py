import streamlit as st
import json
import requests

with st.form("Insert fruit"):
   st.write("Inside the form")
   fruit = st.text_input("Fruit", '')

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       # x = requests.post(url, json = myobj)
       requests.post(f"http://localhost:8000/add/{fruit}")
       fruits = requests.get("http://localhost:8000/list")
       st.write("slider", fruits.text)