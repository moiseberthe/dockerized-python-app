import streamlit as st
import requests

with st.form("Insert fruit"):
    st.header("🍇 Ajouter un fruit")
    fruit = st.text_input("Fruit")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Add new fruit 
        requests.post(f"http://server:8000/add/{fruit}")

        # get all fruits
        fruits = requests.get("http://server:8000/list")
        st.write(fruits.json())

iris_tab, penguin_tab = st.tabs([ "🌻 Iris", "🐧 Penguin"])

with iris_tab:
    st.header("Prédiction Iris")
    with st.form("Prédire Iris"):
        
        sepal_length = st.slider('Sepal length', 0, 10, 0)
        sepal_width = st.slider('Sepal width', 0, 10, 0)

        petal_length = st.slider('Petal length', 0, 10, 0)
        petal_width = st.slider('Petal width', 0, 10, 0)

        submitter = st.form_submit_button("Prédire")

        if submitter:
            # call api
            prediction = requests.get(f"http://server:8000/predict/iris/{sepal_length}/{sepal_width}/{petal_length}/{petal_width}")
            st.write(prediction.json())

with penguin_tab:
    st.header("Prédiction Penguins")
    with st.form("Prédire Penguin"):
        
        col1, col2 = st.columns(2)
        with col1:
            island = st.selectbox(
                'Island',
                ('Torgersen', 'Biscoe', 'Dream')
            )
        with col2:
            sex = st.selectbox(
                'Gender',
                ('male', 'female')
            )
        
        col1, col2 = st.columns(2)
        with col1:
            bill_length_mm = st.number_input('Bill length (mm)')
        with col2:
            bill_depth_mm = st.number_input('Bill depth (mm)')
        
        col1, col2 = st.columns(2)
        with col1:
            flipper_length_mm = st.number_input('Flipper length (mm)')
        with col2:
            body_mass_g = st.number_input('Body mass (g)')

        
        # Every form must have a submit button.
        submitter = st.form_submit_button("Prédire")

        if submitter:
            # call api
            prediction = requests.get(f"http://server:8000/predict/penguins/{island}/{bill_length_mm}/{bill_depth_mm}/{flipper_length_mm}/{body_mass_g}/{sex}")
            st.write(prediction.json())