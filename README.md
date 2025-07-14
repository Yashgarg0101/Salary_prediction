# 💼 Salary Prediction Web App

This repository hosts a machine learning-powered Streamlit web application that predicts salaries (in USD) based on job-related features.

Project URL: https://salaryprediction-c2qcd4cwfnftblm7jthb79.streamlit.app/
---

## 🔍 Overview

This app allows users to input various job attributes and returns a predicted salary using a trained ensemble model built with Scikit-learn. It's designed for educational, prototyping, or hiring insights.

---

## 🧠 Features

- 📊 Predicts salary using multiple input parameters
- 🧠 Uses an ensemble of **Linear Regression**, **Random Forest**, and **Gradient Boosting**
- 🎯 High Accuracy: **R² Score: 0.9169**
- 🌐 Built with Python, Streamlit, and Scikit-learn

---

## 🎛️ Input Parameters

The user selects or provides values for the following:

| Input Field         | Type     | Description                                                  |
|---------------------|----------|--------------------------------------------------------------|
| `Job Title`         | Dropdown | Example: Machine Learning Scientist, Data Analyst, etc.      |
| `Company Size`      | Dropdown | Company size: Small (`S`), Medium (`M`), Large (`L`)         |
| `Employee Residence`| Dropdown | Country/region of the employee (e.g., US, GB, IN, etc.)      |
| `Experience Level`  | Dropdown | Entry (`EN`), Mid (`MI`), Senior (`SE`), Executive (`EX`)     |
| `Employment Type`   | Dropdown | Full-time (`FT`), Part-time (`PT`), Freelance (`FL`), Contract (`CT`) |

These values are dynamically loaded from the dataset (`dropdown_options.pkl`).

---

## 📈 Model Performance

- ✅ **R² Score**: 0.9169  
- ✅ **RMSE**: 18,279.95  
- ✅ **MAE**: 11,594.54  

---

## 🛠 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/salary-prediction-app.git
cd salary-prediction-app
