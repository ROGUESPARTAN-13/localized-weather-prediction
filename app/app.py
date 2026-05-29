import streamlit as st
import pickle
import pandas as pd
import os

# Get current file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model paths
model_path = os.path.join(BASE_DIR, "..", "models", "weather_model.pkl")
encoder_path = os.path.join(BASE_DIR, "..", "models", "label_encoder.pkl")

# Load model and encoder
model = pickle.load(open(model_path, "rb"))
encoder = pickle.load(open(encoder_path, "rb"))

# App Title
st.title("🌦 Weather Prediction App")

st.write("Enter weather details below:")

# User Inputs
precipitation = st.number_input("Precipitation", value=0.0)
temp_max = st.number_input("Maximum Temperature", value=20.0)
temp_min = st.number_input("Minimum Temperature", value=10.0)
wind = st.number_input("Wind Speed", value=3.0)

year = st.number_input("Year", value=2015)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
day = st.number_input("Day", min_value=1, max_value=31, value=1)

# Prediction Button
if st.button("Predict Weather"):

    data = pd.DataFrame(
        [[
            precipitation,
            temp_max,
            temp_min,
            wind,
            year,
            month,
            day
        ]],
        columns=[
            "precipitation",
            "temp_max",
            "temp_min",
            "wind",
            "year",
            "month",
            "day"
        ]
    )

    prediction = model.predict(data)

    weather = encoder.inverse_transform(prediction)

    st.success(f"Predicted Weather: {weather[0]}")