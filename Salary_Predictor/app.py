import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Salary Predictor", layout="centered")

st.title("💰 Salary Predictor")
st.write("Enter your experience to estimate salary")

# Input
exp = st.slider("Years of Experience", 0, 20, 1)

if st.button("Predict Salary"):
    prediction = model.predict([[exp]])[0]

    # Convert values
    salary_yearly = prediction
    salary_lpa = salary_yearly / 100000
    salary_monthly = salary_yearly / 12

    st.success(f"💰 Estimated Salary: ₹{salary_yearly:,.0f}")
    st.info(f"📊 {salary_lpa:.2f} LPA")
    st.info(f"📅 ₹{salary_monthly:,.0f} per month")