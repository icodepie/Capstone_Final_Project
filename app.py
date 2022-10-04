import streamlit as st
import pandas as pd
import pickle

st.write("# Credit score simulator")

st.write("## Describe inputs")

col_names = ['Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
       'Num_Credit_Card', 'Num_of_Loan', 'Num_Credit_Inquiries', 'Credit_Mix',
       'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Credit_History_Age',
       'Payment_of_Min_Amount', 'Amount_invested_monthly']
     
age = st.selectbox(label="Select age", options=range(10, 100))

annual_income = st.slider(label="Annual income", min_value=0, max_value=500000, value=100000, step=500)

monthly_inhand_salary = st.slider(label="Monthly inhand salary", min_value=0, max_value=30000, value=10000, step=100)

num_bank_accounts = st.slider(label="Number of bank accounts", min_value=0, max_value=15, value=1, step=1)

num_credit_card = st.slider(label="Number of credit cards", min_value=0, max_value=25, value=1, step=1)

num_of_loan = st.slider(label="Number of loans", min_value=0, max_value=20, value=1, step=1)

num_credit_inquiries = st.slider(label="Number of credit inquiries", min_value=0, max_value=20, value=1, step=1)

credit_mix = st.selectbox(label="Credit mix", options=["Good", "Bad","Standard"])

outstanding_debt = st.slider(label="Outstanding debt", min_value=0, max_value=250000, value=100000, step=100)

credit_utilization_ratio = st.slider(label="Credit utilization ratio", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

credit_history_age = st.slider(label="Credit history age", min_value=0, max_value=60, value=10, step=1)

payment_of_min_amount = st.selectbox(label="Payment of minimum amount", options=["Yes", "No"])

amount_invested_monthly = st.slider(label="Amount invested monthly", min_value=0, max_value=20000, value=10000, step=50)


if st.button("Click for Rating"):

    input_row = [age, annual_income, monthly_inhand_salary, num_bank_accounts, num_credit_card, num_of_loan, num_credit_inquiries, credit_mix, outstanding_debt, credit_utilization_ratio, credit_history_age, payment_of_min_amount, amount_invested_monthly]

    input = new_test_sample = pd.DataFrame(dict(zip(col_names,input_row)),index=[0])
    st.write(input)

    loaded_model = pickle.load(open("xgb_final_model.sav", 'rb'))
    st.write(loaded_model.predict(input))