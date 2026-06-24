import streamlit as st
import numpy as np
import joblib 
from datetime import datetime

le_crop=joblib.load("/content/drive/MyDrive/ml/le_crop.pkl")
le_soil=joblib.load("/content/drive/MyDrive/ml/le_soil.pkl")
le_fertilizer=joblib.load("/content/drive/MyDrive/ml/le_fertilizer.pkl")
scalar=joblib.load("/content/drive/MyDrive/ml/scaler.pkl")
rf_model=joblib.load("/content/drive/MyDrive/ml/random_forest_fertilizer_model.pkl")


st.title("🌱 Fertilizer Recommendation Agent")

st.write("Enter farm details below:")

# User Inputs
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
moisture = st.number_input("Moisture (%)", min_value=0.0)
soil_type = st.selectbox(
    "Soil Type",
    le_soil.classes_
)

crop_type = st.selectbox(
    "Crop Type",
    le_crop.classes_
)
nitrogen = st.number_input("Nitrogen")
potassium = st.number_input("Potassium")
phosphorous = st.number_input("Phosphorous")

if st.button("Recommend Fertilizer"):

    soil_encoded = le_soil.transform([soil_type])[0]
    crop_encoded = le_crop.transform([crop_type])[0]
    input_data = pd.DataFrame([[
        temperature,
        humidity,
        moisture,
        soil_encoded,
        crop_encoded,
        nitrogen,
        potassium,
        phosphorous
    ]], columns=[
        'Temparature',
        'Humidity',
        'Moisture',
        'Soil Type',
        'Crop Type',
        'Nitrogen',
        'Potassium',
        'Phosphorous'
    ])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    fertilizer_name = le_fertilizer.inverse_transform(prediction)[0]

    st.success(f"Recommended Fertilizer: {fertilizer_name}")

    # Simple schedule generation
    st.subheader("📅 Application Schedule")

    schedule = f"""
    Week 1: Apply {fertilizer_name} at recommended dosage.

    Week 3: Monitor crop growth and soil nutrients.

    Week 5: Reapply {fertilizer_name} if nutrient deficiency is observed.

    Week 8: Final nutrient assessment.
    """

    st.write(schedule)

    # Save farm record
    record = pd.DataFrame([{
        "Date": datetime.now(),
        "Temperature": temperature,
        "Humidity": humidity,
        "Moisture": moisture,
        "Soil Type": soil_type,
        "Crop Type": crop_type,
        "Nitrogen": nitrogen,
        "Potassium": potassium,
        "Phosphorous": phosphorous,
        "Recommended Fertilizer": fertilizer_name
    }])

    try:
        old_records = pd.read_csv("farm_records.csv")
        updated_records = pd.concat([old_records, record])
        updated_records.to_csv("farm_records.csv", index=False)
    except:
        record.to_csv("farm_records.csv", index=False)

    st.success("Farm record saved successfully!")

# View records
st.subheader("📋 Farm Records")

try:
    records = pd.read_csv("farm_records.csv")
    st.dataframe(records)
except:
    st.info("No records available yet.")
