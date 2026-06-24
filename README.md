# Fertilizer Recommendation Agent

## Project Overview

The Fertilizer Recommendation Agent is an intelligent agricultural system developed using Machine Learning and Artificial Intelligence. The system recommends the most suitable fertilizer based on soil properties, environmental conditions, and crop requirements. It helps farmers make informed decisions, improve crop productivity, and manage farm records efficiently.

## Objectives

* Recommend suitable fertilizers based on soil and crop data.
* Compare multiple machine learning models for fertilizer prediction.
* Generate fertilizer application schedules.
* Maintain digital farm management records.
* Provide a user-friendly interface for farmers.

## Dataset

Dataset Used: Fertilizer Prediction Dataset

Features:

* Temperature
* Humidity
* Moisture
* Soil Type
* Crop Type
* Nitrogen
* Potassium
* Phosphorous

Target Variable:

* Fertilizer Name

## Phase 1: Machine Learning Model Development

The following machine learning algorithms were trained and evaluated:

1. Random Forest
2. XGBoost
3. Support Vector Machine (SVM)
4. K-Nearest Neighbors (KNN)
5. Multi-Layer Perceptron (MLP)

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The best-performing model was selected for deployment in the AI Agent.

## Phase 2: AI Agent Development

The AI Agent performs the following tasks:

### Fertilizer Recommendation

Predicts the most suitable fertilizer using the trained machine learning model.

### Application Schedule Generation

Provides a basic fertilizer application schedule to assist farmers in nutrient management.

### Farm Record Management

Stores and displays farm records, including crop details, soil information, and fertilizer recommendations.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib
* Matplotlib
* Seaborn

## Project Structure

Fertilizer-Agent/

├── app.py

├── fertilizer_model.pkl

├── crop_encoder.pkl

├── soil_encoder.pkl

├── fertilizer_encoder.pkl

├── scaler.pkl

├── requirements.txt

├── farm_records.csv

└── README.md

## Installation

Install the required libraries:

pip install -r requirements.txt

## Running the Application

Run the Streamlit application using:

streamlit run app.py

The application will open in a web browser where users can enter soil and crop details to receive fertilizer recommendations.

## Expected Outcomes

* Accurate fertilizer recommendations.
* Improved fertilizer management.
* Digital farm record maintenance.
* Support for better agricultural decision-making.

## Future Enhancements

* Integration with weather forecasting systems.
* Mobile application development.
* Personalized fertilizer dosage recommendations.
* Multilingual support for farmers.

## Author

Project developed as part of the CSP/AI-based Agricultural Management Project.
