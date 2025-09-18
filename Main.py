import streamlit as st
import sklearn as sk
import pandas as pd
import pickle

# Load your trained pipeline (pointing to models/ folder)
with open("model/final_pipeline_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌾 Crop Yield Prediction App")

st.write("Enter the details below to predict the crop yield:")

# Input fields
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, value=450.0)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=34.0)
days_to_harvest = st.number_input("Days to Harvest", min_value=1, max_value=365, value=98)

region = st.selectbox("Region", ["East", "West", "North", "South"])
soil_type = st.selectbox("Soil Type", ["Chalky", "Clay", "Loam", "Peaty", "Sandy", "Silt"])
crop = st.selectbox("Crop", ["Barley", "Cotton", "Maize", "Rice", "Soybean", "Wheat"])
weather = st.selectbox("Weather Condition", ["Cloudy", "Rainy", "Sunny"])

# Prediction button
if st.button("Predict Yield"):
    # Convert input into DataFrame
    input_data = pd.DataFrame([{
        "Rainfall_mm": rainfall,
        "Temperature_Celsius": temperature,
        "Days_to_Harvest": days_to_harvest,
        "Region": region,
        "Soil_Type": soil_type,
        "Crop": crop,
        "Weather_Condition": weather
    }])

    # Predict
    prediction = model.predict(input_data)[0]

    st.success(f"🌱 Predicted Crop Yield: *{prediction:.2f}*")