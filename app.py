import os
import joblib
import streamlit as st
import pandas as pd
import numpy as np


model = joblib.load("C://Users/honer/Downloads/CaloriesBurnedML/final_model.pkl")
scaler = joblib.load("C://Users/honer/Downloads/CaloriesBurnedML/final_scaler.pkl")
converter = joblib.load("C://Users/honer/Downloads/CaloriesBurnedML/final_poly_converter.pkl")


st.title("Predicting calories burned during an exercise.")

col1, col2, col3 = st.columns(3)

with col1:
    Age = st.text_input('Age')

with col2:
    Height = st.text_input('Height in cm')

with col3:
    Weight = st.text_input('Weight in kg')

with col1:
    Duration = st.text_input('Duration of exercise in minutes')

with col2:
    Heart_Rate = st.text_input('Heart rate (bps)')

with col3:
    Body_Temp = st.text_input('Average body temp (celsius)')

with col1:
    Gender = st.text_input('Gender (M or F)')


if st.button('Calories Burned: '):
    Gender = "1" if Gender == "M" else "0"
    user_input = [[int(f) for f in [Age, Height, Weight, Duration, Heart_Rate, Body_Temp, Gender]]]

    poly_features = converter.transform(user_input)
    scaled_input = scaler.transform(poly_features)
    prediction = np.round(model.predict(scaled_input), 1)[0]

    st.success(prediction)


