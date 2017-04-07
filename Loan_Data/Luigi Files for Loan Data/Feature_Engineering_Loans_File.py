
# coding: utf-8

# # Feature Engineering of Lending Club

# In[80]:

import pandas as pd
import numpy as np
import seaborn
from sklearn.decomposition import PCA
from pandas.tools.plotting import scatter_matrix
from sklearn import preprocessing


# In[96]:

def feature_engineering():
    validated_dataframe = pd.read_csv("LoanStats_Validated.csv",sep=',')
    featured_df = pd.DataFrame()
    featured_df = validated_dataframe.drop(['total_bal_il','il_util','open_rv_12m','mths_since_recent_revol_delinq','mths_since_recent_bc_dlq','open_acc_6m','open_il_6m','open_il_12m','open_il_12m','open_il_24m','mths_since_rcnt_il','desc','mths_since_last_record','mths_since_last_major_derog','annual_inc_joint','dti_joint','verification_status_joint'], axis =1)
    featured_df = featured_df.drop(['url','file_name','time_stamp','id','title','grade','emp_title','zip_code'], axis =1)
    featured_df['sub_grade_category'] = pd.factorize(featured_df.sub_grade)[0]
    featured_df['sub_grade_category'] = featured_df['sub_grade_category'].astype('category')
    featured_df['emp_length_category'] = pd.factorize(featured_df.emp_length)[0]
    featured_df['emp_length_category'] = featured_df['emp_length_category'].astype('category')
    featured_df['home_ownership_category'] =  pd.factorize(featured_df.home_ownership)[0]
    featured_df['home_ownership_category'] = featured_df['home_ownership_category'].astype('category')
    featured_df['Loan_status_category'] = pd.factorize(featured_df.loan_status)[0]
    featured_df['Loan_status_category'] = featured_df['Loan_status_category'].astype('category')
    featured_df['addr_state_category'] = pd.factorize(featured_df.addr_state)[0]
    featured_df['addr_state_category'] = featured_df['addr_state_category'].astype('category')
    featured_df['loan_purpose_category'] = pd.factorize(featured_df.purpose)[0]
    featured_df['loan_purpose_category'] = featured_df['loan_purpose_category'].astype('category')
    featured_df['verification_status_category'] = pd.factorize(featured_df.verification_status)[0] 
    featured_df['verification_status_category'] = featured_df['verification_status_category'].astype('category')
    featured_df['application_type_category'] = pd.factorize(featured_df.application_type)[0]
    featured_df['application_type_category'] = featured_df['application_type_category'].astype('category')
    featured_df['policy_code'] = featured_df['policy_code'].astype('category')
    featured_df['term'] = pd.factorize(featured_df.term)[0]
    featured_df['term'] = featured_df['term'].astype('category')
    featured_df['loan_amnt_normalize'] = preprocessing.normalize(featured_df.loan_amnt)[0]
    featured_df['funded_amnt_inv_normalize'] = preprocessing.normalize(featured_df.funded_amnt_inv)[0]
    featured_df['annual_inc_normalize'] = preprocessing.normalize(featured_df.annual_inc)[0]
    featured_df['dti_normalize'] = preprocessing.normalize(featured_df.loan_amnt)[0]
    featured_df['total_pymnt_normalize'] = preprocessing.normalize(featured_df.total_pymnt)[0]
    featured_df['total_pymnt_inv_normalize'] = preprocessing.normalize(featured_df.total_pymnt_inv)[0]
    featured_df['total_acc_normalize'] = preprocessing.normalize(featured_df.total_acc)[0]
    featured_df['revol_bal_normalize'] = preprocessing.normalize(featured_df.revol_bal)[0]
    featured_df['revol_util_normalize'] = preprocessing.normalize(featured_df.revol_util)[0]
    print("Saving the validated file in a csv..")
    featured_df.to_csv('LoanStats_Featured.csv',index=None)
    print("Succeffully saved..")
    


# In[ ]:



