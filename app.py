import streamlit as st
import joblib
import numpy as np

model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction App")

pregnancies = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose", 0, 300)
blood_pressure = st.number_input("Blood Pressure", 0, 200)
skin_thickness = st.number_input("SkinThickness",0,100)
insulin = st.number_input("Insulin",0,250)
bmi = st.number_input("BMI", 0.0, 70.0)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction",0.0,10.0)
age = st.number_input("Age", 1, 120)

if st.button("Predict"):

    features = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        DiabetesPedigreeFunction,
        age
    ]])

    prediction = model.predict(features)

    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"High Diabetes Risk ({probability:.2%})")
    else:
        st.success(f"Low Diabetes Risk ({probability:.2%})")