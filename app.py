import streamlit as st
import pandas as pd
import pickle
import numpy as np
from streamlit.state.session_state import Serialized

st.title("Attrition of Employees Predictor")
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Employee Attrition Prediction ML App </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
st.write("### Information of the beneficary")

model=open('Attrition_saved_model','rb')
model=pickle.load(model)


input = []
# City
S = st.selectbox('City', ['Pune', 'Noida', 'Bangalore', 'Lucknow', 'Chennai', 'Hyderabad', 'Nagpur',
 'Madurai', 'Mumbai', 'Gurgaon', 'Kolkata', 'Vijayawada'])
if S == 'Pune':
    S_result = 10
if S == 'Noida':
    S_result = 9
if S == 'Bangalore':
    S_result = 0
if S == 'Lucknow':
    S_result = 5
if S == 'Chennai':
    S_result = 1
if S == 'Hyderabad':
    S_result = 3
if S == 'Nagpur':
    S_result = 8
if S == 'Madurai':
    S_result = 6
if S == 'Mumbai':
    S_result = 7
if S == 'Gurgaon':
    S_result = 2
if S == 'Kolkata':
    S_result = 4
if S == 'Vijayawada':
    S_result = 11
input.append(S_result)

# Emp Group
C = st.selectbox('Employment Group', ['B2', 'B7', 'B3', 'B1', 'B5', 'B0', 'B4', 'B6', 'C3', 'D2'])
if C == 'B2':
    C_result = 2
if C == 'B7':
    C_result = 7
if C == 'B3':
    C_result = 3
if C == 'B1':
    C_result = 1
if C == 'B5':
    C_result = 5
if C == 'B0':
    C_result = 0
if C == 'B4':
    C_result = 4
if C == 'B6':
    C_result = 6
if C == 'C3':
    C_result = 8
if C == 'D2':
    C_result = 9

input.append(C_result)

# Function
F = st.radio("Function", ('Operation', 'Support', 'Sales'))
if F == 'Operation':
    F_result = 0
if F == 'Support':
    F_result = 2
if F == 'Sales':
    F_result = 1
input.append(F_result)

# Gender
G = st.radio("Gender", ('Male', 'Female', 'other'))
if G == 'Male':
    G_result = 1
if G == 'Female':
    G_result = 0
if G == 'other':
    G_result = 2
input.append(G_result)

# Tenure Group
TG = st.radio("Tenure Group", ('< =1', '> 1 & < =3'))
if TG == '< =1':
    TG_result = 0
if TG == '> 1 & < =3':
    TG_result = 1
input.append(TG_result)

# Age
input.append(st.text_input('Enter the age'))

# Experience
input.append(st.text_input('Enter the experience'))

# Marital Status
MS = st.selectbox("Marital Status", ['Single', 'Married', 'Divided', 'Needs to be Decided', 'Separated'])
if MS == 'Single':
    MS_result = 4
if MS == 'Married':
    MS_result = 1
if MS == 'Divided':
    MS_result = 0
if MS == 'Needs to be Decided':
    MS_result = 2
if MS == 'Separated':
    MS_result = 3
input.append(TG_result)

# Promoted/NonPromoted
P = st.radio("Promoted/NonPromoted", ('Non Promoted', 'Promoted'))
if P == 'Non Promoted':
    P_result = 0
if P == 'Promoted':
    P_result = 1
input.append(P_result)

# HiringSource
HS = st.selectbox("Hiring Source", ('Direct', 'Agency', 'Employee Referral'))
if HS == 'Direct':
    HS_result = 1
if HS == 'Agency':
    HS_result = 0
if HS == 'Employee Referral':
    HS_result = 2
input.append(HS_result)


# JobRoleMatch
Q = st.radio("Job Role Match", ('Yes', 'No'))
if Q == 'Yes':
    Q_result = 1
if Q == 'No':
    Q_result = 0
input.append(Q_result)


# Prediction
try:
    if st.button("Predict"):
        p = model.predict([input])
        if p==1:
            st.success(f"The employee will stay")
        else:
            st.success(f"The employee will not stay")
except:
    st.error("Please try again")