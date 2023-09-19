#main.py


import streamlit as st
import pandas as pd
import os
import io
from form import run
import hashlib

# Define your page names
PAGE_MAIN = "Select Your PinCode"
PAGE_LOGIN = "Login"
PAGE_FORM = "Form Page"
PAGE_DASHBOARD = "Dashboard Page"

# Initialize the session state
if "current_page" not in st.session_state:
    st.session_state.current_page = PAGE_MAIN

if "selected_pincode" not in st.session_state:
    st.session_state.selected_pincode = None

st.title("Select Option")

# Option button for the main page, login, and form
option = st.radio("Select an option", [PAGE_MAIN, PAGE_FORM, PAGE_LOGIN])

df = pd.read_csv("pincode.csv")
pincode_list = df["pincode"]

if option != st.session_state.current_page:
    st.session_state.current_page = option


os.chdir(r"D:\Mortgage Streamlit")
df = pd.read_csv("pincode.csv")

if st.session_state.current_page == PAGE_MAIN:
    st.subheader("Enter Pincode")
    selected_pincode = st.selectbox("Select Pincode", df["pincode"].unique())

    if st.button("Submit"):
        st.session_state.selected_pincode = selected_pincode  # Store the selected pincode
        selected_data = df[df["pincode"] == selected_pincode]

        st.subheader("PinCode Info")
        st.write(f'Pincode: {selected_pincode}')
        st.write(f'City: {selected_data["city"].unique()}')
        st.write(f'State: {selected_data["state_name"].unique()}')

        show_register_button = True

        if show_register_button:
            st.write("You can register as a new user.")
            if st.button("Register"):
                st.session_state.form_page = PAGE_FORM  

# For user login
elif st.session_state.current_page == PAGE_LOGIN:
    st.subheader("User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Checking username and password from data
        existing_df = pd.read_csv("user_data.csv")  # Loading user_data

        user_match = existing_df[(existing_df["Username"] == username) & (existing_df["Password Hash"] == hashlib.sha256(password.encode()).hexdigest())]

        if not user_match.empty:
            st.success("Login successful!")
            # Add code to navigate to another page

            if st.button("Go to Dashboard"):
                st.session_state.current_page = PAGE_DASHBOARD

        else:
            st.error("Login failed. Incorrect username or password.")

# For dashboard page
elif st.session_state.current_page == PAGE_DASHBOARD:
    st.subheader("Dashboard Page")
    # Add your dashboard content here

elif st.session_state.current_page == PAGE_FORM:
    run()
