import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('credit_risk_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("💳 Credit Risk Predictor")
st.write("Fill in the applicant details below to predict default risk.")

age = st.slider("Age", 18, 70, 30)
income = st.number_input("Annual Income ($)", min_value=0, value=50000)
loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=10000)
credit_score = st.slider("Credit Score", 300, 850, 650)
employment_years = st.slider("Years Employed", 0, 40, 5)
education = st.selectbox("Education Level", ["High School", "Bachelors", "Masters", "PhD"])
housing = st.selectbox("Housing Status", ["Mortgage", "Own", "Rent"])

education_map = {"High School": 0, "Bachelors": 1, "Masters": 2, "PhD": 3}
education_val = education_map[education]
housing_own = 1 if housing == "Own" else 0
housing_rent = 1 if housing == "Rent" else 0

if st.button("Predict"):
    input_df = pd.DataFrame([[age, income, loan_amount, credit_score,
                               employment_years, education_val, 0,
                               housing_own, housing_rent]],
                            columns=['Age', 'Income', 'Loan_Amount', 'Credit_Score',
                                     'Employment_Years', 'Education_Level', 'Default',
                                     'Housing_Status_Own', 'Housing_Status_Rent'])

    input_scaled = scaler.transform(input_df)
    input_final = pd.DataFrame(input_scaled, columns=input_df.columns).drop(columns='Default')

    prob = model.predict_proba(input_final)[0][1]

    st.divider()
    if prob >= 0.5:
        st.error(f"⚠️ High Risk of Default — Probability: {round(prob*100, 1)}%")
    else:
        st.success(f"✅ Low Risk of Default — Probability: {round(prob*100, 1)}%")