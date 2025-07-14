
import streamlit as st
import pandas as pd
import joblib

# Load model and metadata
model = joblib.load("salary_predictor.pkl")
model_columns = joblib.load("model_columns.pkl")
dropdown_options = joblib.load("dropdown_options.pkl")

st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Prediction Web App")
st.markdown("Use this app to predict salaries (in USD) based on job-related information.")

# Sidebar input
st.sidebar.header("Enter Job Details")
job_title = st.sidebar.selectbox("Job Title", dropdown_options["job_title"])
company_size = st.sidebar.selectbox("Company Size", dropdown_options["company_size"])
employee_residence = st.sidebar.selectbox("Employee Residence", dropdown_options["employee_residence"])
experience_level = st.sidebar.selectbox("Experience Level", dropdown_options["experience_level"])
employment_type = st.sidebar.selectbox("Employment Type", dropdown_options["employment_type"])

# Prepare input
input_data = pd.DataFrame([{
    "job_title": job_title,
    "company_size": company_size,
    "employee_residence": employee_residence,
    "experience_level": experience_level,
    "employment_type": employment_type
}])

input_encoded = pd.get_dummies(input_data)
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"💰 Predicted Salary: ${int(prediction):,} USD")

st.markdown("---")
st.markdown("🔧 Built using Streamlit & Machine Learning")
