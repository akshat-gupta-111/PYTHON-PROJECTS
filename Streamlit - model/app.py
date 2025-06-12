import streamlit as st
import numpy as np
import pandas as pd
import joblib as jl
import base64

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("bg.jpeg")

model = jl.load('aircraft.pkl')

st.title("Fuel Consumption in Aircraft")
st.write("This dashboard helps predict fuel consumption based on distance, duration, passenger count, and aircraft type.")

fd = st.number_input("Flight Distance (in km):", min_value=0.0)
npax = st.number_input("Number of Passengers:", min_value=0)
du = st.number_input("Flight Duration (in hours):", min_value=0.0)
ft = st.selectbox("Aircraft Type:", ["T1", "T2", "T3"])

input_data = pd.DataFrame(
    {
        'Flight_Distance': [fd],
        'Number_of_Passengers': [npax],
        'Flight_Duration': [du],
        'Aircraft_Type_Type1': [1 if ft == "T1" else 0],
        'Aircraft_Type_Type2': [1 if ft == "T2" else 0],
        'Aircraft_Type_Type3': [1 if ft == "T3" else 0],
    }
)

if st.button('Predict'):
    fc = model.predict(input_data)
    st.success(f'Predicted Fuel Consumption: {fc[0][0]:.2f} liters')
    st.caption("Prediction based on input parameters using trained ML model.")