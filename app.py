import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="Telco Customer Churn & Retention Platform",
    page_icon="📉",
    layout="wide"
)

st.title("📉 Telco Customer Churn Prediction & Retention Analytics System")
st.markdown("---")

# Welcome Section
st.subheader("Welcome to the Churn Analytics Dashboard!")
st.write("""
This application helps telecom operators analyze customer data, predict churn risks, 
and deploy targeted retention strategies. Use the sidebar to navigate through different modules:
""")

# Quick Status Check
data_path = "DATA/WA_Fn-UseC_-Telco-Customer-Churn.csv"
if os.path.exists(data_path):
    st.success(" Dataset (`WA_Fn-UseC_-Telco-Customer-Churn.csv`) successfully detected inside the `DATA/` folder!")
else:
    st.warning(" Dataset not found! Please ensure `WA_Fn-UseC_-Telco-Customer-Churn.csv` is placed inside the `DATA/` folder.")

st.info(" Please select a page from the left sidebar to begin exploring the platform.")