import streamlit as st

st.title("loan Approval App")
client_name = st.text_input("enter your name:")
income = st.number_input("enter your monthly income:")
credit_score = st.number_input("Enter your credit score:")
loan_amount = st.number_input("Enter requested loan amount:")

if st.button("check loan eligibility"):
    if income >90000 and  credit_score >150 and loan_amount >500000:
        st.success(f"congratulations! {client_name} is eligible for the loan.")
    else:
        st.error(f"sorry ,{client_name} is not eligible for the loan.")