
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import os


# # Validation function

# In[2]:

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

print("The end..")

