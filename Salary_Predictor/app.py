import os
import sys
import streamlit as st
import pickle

# Ensure correct path
sys.path.append(os.path.dirname(__file__))

# Auto-train model if not exists
if not os.path.exists("model.pkl"):
    import train

# Load model
model = pickle.load(open("model.pkl", "rb"))

# UI setup
st.set_page_config(page_title="Salary Predictor", layout="centered")

st.title("💰 Salary Predictor")
st.write("Enter your experience to estimate salary")

# Input
exp = st.slider("Years of Experience", 0, 20, 1)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict([[exp]])[0]

    salary_yearly = prediction
    salary_lpa = salary_yearly / 100000
    salary_monthly = salary_yearly / 12

    st.success(f"💰 Estimated Salary: ₹{salary_yearly:,.0f}")
    st.info(f"📊 {salary_lpa:.2f} LPA")
    st.info(f"📅 ₹{salary_monthly:,.0f} per month")

    # Optional celebration 🎈
    st.balloons()
