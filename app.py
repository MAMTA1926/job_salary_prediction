import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("job_salary.pkl")

st.title("Salary Prediction App")

# 👇 YOUR CODE GOES HERE
job_title = st.selectbox("Job Title", [
    "AI Engineer","Data Analyst","Data Scientist",
    "Software Engineer","Frontend Developer","Backend Developer",
    "Business Analyst","Product Manager"
])

education = st.selectbox("Education", [
    "High School","Diploma","Bachelor","Master","PhD"
])

industry = st.selectbox("Industry", [
    "Technology","Healthcare","Finance","Retail",
    "Manufacturing","Consulting","Telecom","Media"
])

company_size = st.selectbox("Company Size", [
    "Startup","Small","Medium","Large","Enterprise"
])

location = st.selectbox("Location", [
    "India","USA","UK","Canada","Australia","Germany","Singapore","Sweden"
])

remote = st.selectbox("Remote Work", [
    "Yes","No","Hybrid"
])

experience = st.slider("Experience", 0, 20)
skills = st.slider("Skills Count", 1, 20)
certifications = st.slider("Certifications", 0, 10)

# Create input dataframe
input_data = pd.DataFrame([{
    'job_title': job_title,
    'experience_years': experience,
    'education_level': education,
    'skills_count': skills,
    'industry': industry,
    'company_size': company_size,
    'location': location,
    'remote_work': remote,
    'certifications': certifications
}])

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Salary: ₹ {prediction:.2f}")