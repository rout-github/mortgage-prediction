#form.py

import streamlit as st
import pandas as pd
import uuid
import os
import hashlib

pincode_df = pd.read_csv("pincode.csv", usecols=["pincode", "city", "state_name"])

def is_username_unique(username, existing_df):
    return username not in existing_df["Username"].values

def is_email_unique(email, existing_df):
    return email not in existing_df["Email"].values

def run():
    st.title("User Registration Form")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    email = st.text_input("Email Address")
    phone_number = st.text_input("Phone Number")
    address = st.text_area("Address")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    user_id = str(uuid.uuid4())

    if st.button("Submit Form"):
        selected_pincode = st.session_state.selected_pincode
        pincode_info = pincode_df[pincode_df["pincode"] == selected_pincode]

        if not pincode_info.empty:
            city_name = pincode_info["city"].values[0]
            state_name = pincode_info["state_name"].values[0]

            if os.path.exists("user_data.csv"):
                existing_df = pd.read_csv("user_data.csv")
            else:
                existing_df = pd.DataFrame()

            if is_username_unique(username, existing_df) and is_email_unique(email, existing_df):
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                user_data = {
                    "User ID": [user_id],
                    "Name": [name],
                    "Age": [age],
                    "Email": [email],
                    "Username": [username],
                    "Password Hash": [password_hash],
                    "Phone Number": [phone_number],
                    "Address": [address],
                    "Pincode": [selected_pincode],
                    "City": [city_name],
                    "State Name": [state_name]
                }

                new_data = pd.DataFrame(user_data)
                updated_df = pd.concat([existing_df, new_data], ignore_index=True)

                updated_df.to_csv("user_data.csv", index=False)

                st.write("User Registration Details:")
                st.table(updated_df)
                st.write("User data has been saved to user_data.csv")
            else:
                st.write("Username or Email already exists. Please choose a different one.")
        else:
            st.write("Pincode not found")
