import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("Bank_personal_loan.pkl","rb"))

st.title("Bank Loan qualification App")


# Create text inputs for each feature
Age = st.text_input("Age","30")
Income = st.text_input("Income","1000")
Securities_Account = st.text_input("Securities Account","500")
CD_Account = st.text_input("CD Account","200.00")
creditCard = st.text_input("CreditCard","300")

inputs = [float(Age),float(Income),float(Securities_Account),
          float(CD_Account),float(creditCard)]

# predictiion button 
if st.button("Predict"):
    prediction = model.predict([inputs])
    if prediction[0] == 1:
        st.success("The Customer is eligble for a loan")
    else:
        st.error("The Sustomer is not eligible for a loan")