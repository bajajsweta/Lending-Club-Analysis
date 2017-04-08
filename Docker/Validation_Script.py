
# coding: utf-8

# In[4]:

import pandas as pd
import numpy as np
import os
import pandas as pd
import numpy as np
from sklearn import preprocessing


# # Validation function

# In[5]:

## find the number of nan in each column
#Q2.isnull().sum()
## fill na
def validate_field():
    data_frame = pd.read_csv('Combined_data_file.csv')
    print(data_frame.head(2))
    
    Q3 = data_frame[np.isfinite(data_frame['member_id'])]
    Q3['emp_title'].fillna("unknown",inplace=True)
    Q3.mths_since_last_delinq= Q3.mths_since_last_delinq.interpolate()
    Q3['mths_since_recent_bc'] = Q3['mths_since_recent_bc'].interpolate()
    Q3['mths_since_recent_bc_dlq'] =Q3['mths_since_recent_bc_dlq'].interpolate(limit=50)
    Q3['mths_since_recent_inq'] =Q3['mths_since_recent_inq'].interpolate()
    Q3['mths_since_recent_revol_delinq'] =Q3['mths_since_recent_revol_delinq'].interpolate()
    Q3['num_tl_120dpd_2m'] =Q3['num_tl_120dpd_2m'].interpolate()
    Q3['percent_bc_gt_75'] =Q3['percent_bc_gt_75'].interpolate()
    Q3['last_pymnt_d'] = Q3['last_pymnt_d'].fillna('Unknown')
    Q3['next_pymnt_d']= Q3['next_pymnt_d'].fillna('Unknown')
    Q3['last_credit_pull_d'] = Q3['last_credit_pull_d'].fillna('Unknown')
    Q3['mths_since_last_major_derog'].fillna(0,inplace=True)
    Q3['annual_inc_joint'] =Q3['annual_inc_joint'].interpolate()
    Q3['dti_joint'] =Q3['dti_joint'].interpolate()
    Q3['verification_status_joint'].fillna('unknown',inplace=True)
    Q3['mths_since_rcnt_il'] =Q3['mths_since_rcnt_il'].interpolate()
    Q3['il_util'] =Q3['il_util'].interpolate()
    Q3['bc_open_to_buy'] =Q3['bc_open_to_buy'].interpolate()
    Q3['bc_util'] =Q3['bc_util'].interpolate()
    Q3['mo_sin_old_il_acct'].fillna(0,inplace=True)
    Q3['emp_length_clean'] = Q3.emp_length.str.replace('+','')
    Q3['emp_length_clean'] = Q3.emp_length_clean.str.replace('< 1','0')
    Q3['emp_length_clean'] = Q3.emp_length_clean.str.replace('years','')
    Q3['emp_length_clean'] = Q3.emp_length_clean.str.replace('year','')
    Q3['emp_length_clean'] = Q3.emp_length_clean.str.replace('n/a','-1')
    Q3['emp_length_clean'].fillna('-1',inplace=True)
    Q3['emp_length_clean']=pd.to_numeric(Q3['emp_length_clean'], errors='ignore')
    
    Q3['title'].fillna('unknown',inplace=True)
    Q3['mths_since_last_delinq'].fillna(0,inplace=True)
    Q3['desc'].fillna('unknown',inplace=True)
    Q3['mths_since_last_record'].fillna(0,inplace=True) 
    Q3['mths_since_recent_bc_dlq'].fillna(0,inplace=True)
    Q3['mths_since_recent_revol_delinq'].fillna(0,inplace=True)

    #Remove % symbol from the interest rate & revolving utilization
    Q3['revol_util'] = Q3['revol_util'].str.split('%',1).str[0]
    Q3['int_rate'] = Q3['int_rate'].str.split('%',1).str[0]

    ## drop months from the column 
    Q3['term']=Q3['term'].str.split(' ',2).str[1]

    ## fill if any nan left with zero
    Q3.fillna(0,inplace=True)
    
    print("Saving the validated file in a csv..")
    Q3.to_csv('LoanStats_Validated.csv',index=None)
    print("Succeffully saved..")


# In[ ]:

def feature_engineering():
    validated_dataframe = pd.read_csv("LoanStats_Validated.csv")
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
    #featured_df['loan_amnt_normalize'] = preprocessing.normalize(featured_df.loan_amnt)
    #featured_df['funded_amnt_inv_normalize'] = preprocessing.normalize(featured_df.funded_amnt_inv)
    #featured_df['annual_inc_normalize'] = preprocessing.normalize(featured_df.annual_inc)
    #featured_df['dti_normalize'] = preprocessing.normalize(featured_df.loan_amnt)
    #featured_df['total_pymnt_normalize'] = preprocessing.normalize(featured_df.total_pymnt)
    #featured_df['total_pymnt_inv_normalize'] = preprocessing.normalize(featured_df.total_pymnt_inv)
    #featured_df['total_acc_normalize'] = preprocessing.normalize(featured_df.total_acc)
    #featured_df['revol_bal_normalize'] = preprocessing.normalize(featured_df.revol_bal)
    #featured_df['revol_util_normalize'] = preprocessing.normalize(featured_df.revol_util)
    print("Saving the validated file in a csv..")
    featured_df.to_csv('LoanStats_Featured.csv',index=None)
    list(featured_df)
    
    print("Succeffully saved..")
    


# In[ ]:

print("The end..")


# In[ ]:

# In[ ]:



