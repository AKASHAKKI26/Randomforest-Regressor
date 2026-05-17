import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.joblib")

st.title("Airbnb Price Prediction")

latitude = st.number_input(
    "Latitude",
    value=40.7128
)

longitude = st.number_input(
    "Longitude",
    value=-74.0060
)

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    value=2
)

reviews_per_month = st.number_input(
    "Reviews Per Month",
    min_value=0.0,
    value=1.0
)

availability_365 = st.number_input(
    "Availability 365",
    min_value=0,
    max_value=365,
    value=100
)

if st.button("Predict Price"):

    input_data = np.array([[ 
        latitude,
        longitude,
        minimum_nights,
        reviews_per_month,
        availability_365
    ]])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Airbnb Price: ${prediction[0]:.2f}"
    )