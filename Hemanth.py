
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'linear_model.pkl'  # Replace with the actual filename of your saved model
loaded_model = pickle.load(open(filename, 'rb'))

st.title("Monthly Revenue Prediction App")

# Input features
no_of_orders = st.number_input("Number of Orders", min_value=0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
customer_lifetime_value = st.number_input("Customer Lifetime Value", min_value=0.0)
total_customers = st.number_input("Total Customers", min_value=0)
website_traffic = st.number_input("Website Traffic", min_value=0)
marketing_spend = st.number_input("Marketing Spend", min_value=0.0)

if st.button("Predict Revenue"):
    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'no_of_orders': [no_of_orders],
        'avg_order_value': [avg_order_value],
        'customer_lifetime_value': [customer_lifetime_value],
        'total_customers': [total_customers],
        'website_traffic': [website_traffic],
        'marketing_spend': [marketing_spend]
    })

    # Make a prediction using the loaded model
    predicted_revenue = loaded_model.predict(input_data)[0]

    st.write(f"Predicted Monthly Revenue: ${predicted_revenue:.2f}")
