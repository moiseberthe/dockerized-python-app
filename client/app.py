import streamlit as st
import json
import requests

with st.form("Insert fruit"):
    st.write("Fruit form")
    fruit = st.text_input("Fruit", '')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Add new fruit 
        requests.post(f"http://server:8000/add/{fruit}")

        # get all fruits
        fruits = requests.get("http://server:8000/list")
        st.write(fruits.json())
    
with st.form("Predict Iris"):
    st.write("Prediction")
    
    sepal_length = st.slider('Sepal length', 0, 10, 0)
    sepal_width = st.slider('Sepal width', 0, 10, 0)

    petal_length = st.slider('Petal length', 0, 10, 0)
    petal_width = st.slider('Petal width', 0, 10, 0)

    # Every form must have a submit button.
    submitter = st.form_submit_button("Predict")

    if submitter:
        # call api
        prediction = requests.post(f"http://server:8000/predict/{sepal_length}/{sepal_width}/{petal_length}/{petal_width}")
        st.write(prediction.json())

with st.form("Predict Penguin"):
    st.write("Prediction")
    
    island = st.selectbox(
        'Island',
        ('Torgersen', 'Biscoe', 'Dream')
    )
    bill_length_mm = st.number_input('Bill length (mm)')
    bill_depth_mm = st.number_input('Bill depth (mm)')
    flipper_length_mm = st.number_input('Flipper length (mm)')
    body_mass_g = st.number_input('body mass (g)')

    sex = st.selectbox(
        'sex',
        ('male', 'female')
    )
    # Every form must have a submit button.
    submitter = st.form_submit_button("Predict")

    if submitter:
        # call api
        prediction = requests.post(f"http://server:8000/predict_penguins/{island}/{bill_length_mm}/{bill_depth_mm}/{flipper_length_mm}/{body_mass_g}/{sex}")
        st.write(prediction.json())