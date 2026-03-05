import streamlit as st
import joblib
import numpy as np

# Load the model you saved
model = joblib.load('house_model2.pkl')

st.title("House Price Prediction App")

# Create input fields for the user based on your columns
with st.form("prediction_form"):
    st.write("Enter the details below and click 'Predict' when finished.")
    
    # 2. Place all your inputs inside this 'with' block
    median_income = st.number_input("Median Income", value=0.00)
    housing_median_age = st.number_input("Housing Median Age", value=00.0)
    total_rooms_in_house = st.number_input("Total Rooms", value=880.0)
    total_bedrooms_in_house = st.number_input("Total Bedrooms", value=129.0)
    
    submitted = st.form_submit_button("Predict House Price")

# 4. Logic happens ONLY after the button is clicked
if submitted:
    # Arrange inputs in the order used in your notebook (housing q.ipynb)
    features = np.array([[ median_income,housing_median_age, total_rooms_in_house, total_bedrooms_in_house]])
    
    prediction = model.predict(features)
    
    st.success(f"The predicted house price is: ${prediction[0]:,.2f}")
    
# ... add other features from your notebook

