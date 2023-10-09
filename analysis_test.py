import streamlit as st
import requests

st.title("Analysis")

# Input fields for property analysis
purchase_price = st.number_input("Enter the purchase price:", value=0.0)
improvements = st.number_input("Enter the cost of improvements:", value=0.0)
downpayment_amt = st.number_input("Enter the downpayment amount:", value=0.0)
mortgage_years = st.number_input("Enter the mortgage term (in years):", value=30.0)
monthly_rent = st.number_input("Enter the monthly rent:", value=0.0)
vacancy_rate = st.number_input("Enter the vacancy rate (%):", min_value=0.0, max_value=100.0, value=8.33) / 100
annual_maintenance = st.number_input("Enter the annual maintenance cost:", value=0.0)
property_manager_rate = st.number_input("Enter the monthly property manager fee (%):", min_value=0.0, max_value=100.0, value=8.00) / 100
misc_administrative = st.number_input("Enter the monthly miscellaneous administrative fee:", value=0.0)
insurance_rate = st.number_input("Enter the annual insurance rate (%):", min_value=0.0, max_value=100.0, value=0.5) / 100
annual_revenue_increase = st.number_input("Enter the annual revenue increase (%):", min_value=0.0, max_value=100.0, value=5.0) / 100
annual_operating_expense_increase = st.number_input("Enter the annual operating expense increase (%):", min_value=0.0, max_value=100.0, value=2.0) / 100


# Button to calculate
if st.button("Calculate"):
    
    # Prepare the payload with user inputs
    payload = {"improvements": improvements,
               "tax_rate": "1.7%",
               "default_interest_rate": "0.0657%",
               "purchase_price": purchase_price,
                "downpayment_amt": downpayment_amt,
                "zipcode" : 10033,
                "interest_rate" : 6,
                "mortgage_years": mortgage_years,
                "monthly_rent": monthly_rent,
                "vacancy_rate": vacancy_rate,
                "annual_maintenance": annual_maintenance,
                "property_manager_rate": property_manager_rate,
                "misc_administrative": misc_administrative,
                "insurance_rate": insurance_rate,
                "annual_revenue_increase": annual_revenue_increase,
                "annual_operating_expense_increase": annual_operating_expense_increase,
    }

    # Make an API request to the Flask API
    api_url = f"http://127.0.0.1:5000/expenses"
    

    response = requests.get(api_url, json=payload)
    

    if response.status_code == 200 and response.headers['content-type'] == 'application/json':
        data = response.json()
        

        #calculated results
        st.subheader("Calculated Results:")
        
        st.write(f"Gross Income: {data['Gross Income']}")
        st.write(f"Total Expenses: {data['Total Expenses']}")
        st.write(f"Total Cash Flow: {data['Total Cash Flow']}")
        st.write(f"Cash ROI: {data['Cash ROI']}")
        st.write(f"Total Return: {data['Total Return']}")
        st.write(f"Total ROI: {data['Total ROI']}")
        st.write(f"S&P Invest at: {data['S&P invst at']}")
        st.write(f"This Investment: {data['This investment']}")
        st.write(f"Mortgage Cash Flow List: {data['Mortgage cash flow list']}")
        st.write(f"Mortgage S&P Invest at: {data['Mortgage S&P invst at']}")
        st.write(f"Mortgage This Investment: {data['Mortgage This investment']}")
        st.write(f"Investment Analysis: {data['Investment analysis']}")
        st.write(f"Total Cash Flow Results: {data['Total cash flow results']}")

    else:
        
        st.error("Invalid or empty API response.")
