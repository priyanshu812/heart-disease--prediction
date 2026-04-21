import streamlit as st
import pandas as pd 
import joblib

st.title("Heart Disease Prediction ❤️")
st.markdown("Provide the following details to predict the risk of heart disease")
# Load the trained model
model = joblib.load('LogisticRegression.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

#Input field 
age = st.slider("Age",18,100,40,1)
sex = st.radio("Sex", ["Male","Female"])
chest_pain = st.selectbox("Chest Pain Type", ["Typical Angina","Atypical Angina","Non-anginal Pain","Asymptomatic"])
cholestrol = st.number_input("Cholestrol",100,600,200)
resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)",100,200,150)
max_hr = st.slider("Max Heart Rate",60,220,150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes","No"])
oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)
st_slope = st.selectbox("ST Slope", ["Up","Flat","Down"])
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes","No"])
resting_ecg = st.selectbox("Resting ECG", ["Normal","ST-T wave abnormality","Left ventricular hypertrophy"])

# When Predict is clicked
if st.button("Predict"):
    # Create a raw input dictionary
    input_data = {
        'Age': age,
        'RestingBP': resting_blood_pressure,
        'Cholesterol': cholestrol,
        'FastingBS': 1 if fasting_bs == "Yes" else 0,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,

        'Sex_M': 1 if sex == 'Male' else 0,

        'ChestPainType_TA': 1 if chest_pain == 'Typical Angina' else 0,
        'ChestPainType_ATA': 1 if chest_pain == 'Atypical Angina' else 0,
        'ChestPainType_NAP': 1 if chest_pain == 'Non-anginal Pain' else 0,
        'ChestPainType_ASY': 1 if chest_pain == 'Asymptomatic' else 0,

        'ExerciseAngina_Y': 1 if exercise_angina == 'Yes' else 0,

        # ST_Slope (drop-first: Down is base)
        'ST_Slope_Flat': 1 if st_slope == "Flat" else 0,
        'ST_Slope_Up': 1 if st_slope == "Up" else 0,

        # RestingECG (drop-first: LVH is base)
        'RestingECG_Normal': 1 if resting_ecg == "Normal" else 0,
        'RestingECG_ST': 1 if resting_ecg == "ST-T wave abnormality" else 0,
    }

    # Create input dataframe
    input_df = pd.DataFrame([input_data])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match training data
    input_df = input_df[expected_columns]

    # Scale numerical features
    input_scaled = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(input_scaled)[0]
    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")






