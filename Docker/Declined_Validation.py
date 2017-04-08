
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
import requests
import zipfile
from datetime import datetime
import io


# In[16]:

def fill_empty_values():
    df = pd.DataFrame()
    df = pd.read_csv("CombinedRejectLoanStats.csv",delimiter=',', encoding="cp1252")
    df['Amount Requested'].fillna(df['Amount Requested'].mean(), inplace=True)
    df['Application Date'].fillna(method='bfill', inplace=True)
    df['Loan Title'].fillna('NoValue', inplace=True)
    df['Risk_Score'].fillna(0.0, inplace=True)
    df['Zip Code'].fillna('000xx', inplace=True)
    df['Employment Length'].replace('n/a','Unknown years', inplace=True)
    df['Debt-To-Income Ratio'] = df['Debt-To-Income Ratio'].str.split('%',1).str[0]
    df['Debt-To-Income Ratio']=pd.to_numeric(df['Debt-To-Income Ratio'], errors='ignore')
    df['emp_length'] = df['Employment Length'].str.replace('+','')
    df['emp_length'] = df.emp_length.str.replace('< 1','0')
    df['emp_length'] = df.emp_length.str.replace('years','')
    df['emp_length'] = df.emp_length.str.replace('year','')
    df['emp_length'] = df.emp_length.str.replace('n/a','-1')

    df['emp_length']=pd.to_numeric(df['emp_length'], errors='ignore')
    df['Application Year']=df['Application Date'].str[0:4]
    df = df[df.State.notnull()]
    
    df.to_csv('ValidatedCombinedRejectLoan.csv', index=None)
print('Validation done')
    


# def validate_risk_score():
#     df = pd.DataFrame()
#     df = pd.read_csv("CombinedRejectLoanStats.csv",delimiter=',', encoding="cp1252")
#     if any(df['Risk_Score']) not in range(0,1000):
#         print(" Risk Score value out of range")
#     

# def validate_policy_code():
#     df = pd.DataFrame()
#     df = pd.read_csv("CombinedRejectLoanStats.csv",delimiter=',', encoding="cp1252")
#     if any(df['Policy Code'] == 1):
#          print("Wrong policy code data")
#     
