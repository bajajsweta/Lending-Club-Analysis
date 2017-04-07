
# coding: utf-8

# #  Downloading loan files from Lending Club website and merging them into one single dataset 

# In[2]:

import pandas as pd
import os
import glob
import zipfile as z
import numpy as np
from datetime import datetime
import requests
import io


# In[ ]:

print("Scraping data from lending club website.")


# In[ ]:

def download_data():
    s = requests.session()
    letters = 'abcd'
    for each in letters:
        url = 'https://resources.lendingclub.com/LoanStats3'+each+'.csv.zip'
        file1 = s.get(url)
        m1 = z.ZipFile(io.BytesIO(file1.content))
        m1.extractall()
        print("File"+'LoanStats3'+each+'is downloaded..!')
    Quarter = ['Q1','Q2','Q3','Q4']
    for q in Quarter:
        url = 'https://resources.lendingclub.com/LoanStats_2016'+q+'.csv.zip'
        file = s.get(url)
        m = z.ZipFile(io.BytesIO(file.content))
        m.extractall()
        print("File"+'LoanStats_2016'+q+'is downloaded..!')
print("Downloading of csv files is completed..")


# # Merging script beings..

# In[ ]:

print("Merging individual files into one dataset..")
print("Fecthing all the csv files in a list..")


# In[ ]:

def reading_files_to_merge():
    allfiles = glob.glob(os.path.join(os.getcwd(),"*.csv"))

## not reading 3a
    listofFiles= []
    for file in allfiles:
        #print(allfiles[i])
        if 'LoanStats3a'  not in file:
            listofFiles.append(file)
        
    print(listofFiles)    

    np_array_list = []
    for file_ in listofFiles:
        df = pd.DataFrame()
        print("Skipping first two rows as we will be adding the header at the end of merging in order to avoid having multiple headers..")
        df = pd.read_csv(file_,index_col=None,skiprows=range(0, 2))
        print(file_)
        print("Dropping last two rows as we do not need it, they are the total amount funded in policy code 1 and policy code 2 ")
        df= df.drop(df.index[(len(df)-1)])
        df= df.drop(df.index[(len(df)-1)])
        print("This is take a few minutes to complete..")
        #print(df.head(2))
        print("Adding a new column to save the file name..")
        df['file_name'] = file_[-16:-4]
        print("Adding a new column to store the time at which the file was added..")
        df['time_stamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df['Flag'] = 1
        np_array_list.append(df.as_matrix())
    

    comb_np_array = np.vstack(np_array_list)
    big_frame = pd.DataFrame(comb_np_array)
    print("Merge completed successfully..")
    
    print("Adding headers to the merged dataframe..")
    big_frame.columns = ["id", "member_id", "loan_amnt", "funded_amnt",'funded_amnt_inv','term','int_rate','installment','grade','sub_grade','emp_title','emp_length','home_ownership','annual_inc','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','dti','delinq_2yrs','earliest_cr_line','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','initial_list_status','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d','last_pymnt_amnt','next_pymnt_d','last_credit_pull_d','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','application_type','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m','open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m','acc_open_past_24mths','avg_cur_bal','bc_open_to_buy','bc_util','chargeoff_within_12_mths','delinq_amnt','mo_sin_old_il_acct','mo_sin_old_rev_tl_op','mo_sin_rcnt_rev_tl_op','mo_sin_rcnt_tl','mort_acc','mths_since_recent_bc','mths_since_recent_bc_dlq','mths_since_recent_inq','mths_since_recent_revol_delinq','num_accts_ever_120_pd','num_actv_bc_tl','num_actv_rev_tl','num_bc_sats','num_bc_tl','num_il_tl','num_op_rev_tl','num_rev_accts','num_rev_tl_bal_gt_0','num_sats','num_tl_120dpd_2m','num_tl_30dpd','num_tl_90g_dpd_24m','num_tl_op_past_12m','pct_tl_nvr_dlq','percent_bc_gt_75','pub_rec_bankruptcies','tax_liens','tot_hi_cred_lim','total_bal_ex_mort','total_bc_limit','total_il_high_credit_limit','file_name','time_stamp','Flag']
    

    print("Reading LoanStats3a and divding it into two.. based on the loan status value")
    Loan3aDf= pd.read_csv('LoanStats3a.csv', skiprows=[0])
    
    Loan3aDf_1 = Loan3aDf.ix[(Loan3aDf['loan_status']!='Does not meet the credit policy. Status:Charged Off') & (Loan3aDf['loan_status']!='Does not meet the credit policy. Status:Fully Paid')].values
    Df_required_Loan = pd.DataFrame(Loan3aDf_1)

    print("Add column values to the dataframe")
    Df_required_Loan.columns = ["id", "member_id", "loan_amnt", "funded_amnt",'funded_amnt_inv','term','int_rate','installment','grade','sub_grade','emp_title','emp_length','home_ownership','annual_inc','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','dti','delinq_2yrs','earliest_cr_line','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','initial_list_status','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d','last_pymnt_amnt','next_pymnt_d','last_credit_pull_d','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','application_type','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m','open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m','acc_open_past_24mths','avg_cur_bal','bc_open_to_buy','bc_util','chargeoff_within_12_mths','delinq_amnt','mo_sin_old_il_acct','mo_sin_old_rev_tl_op','mo_sin_rcnt_rev_tl_op','mo_sin_rcnt_tl','mort_acc','mths_since_recent_bc','mths_since_recent_bc_dlq','mths_since_recent_inq','mths_since_recent_revol_delinq','num_accts_ever_120_pd','num_actv_bc_tl','num_actv_rev_tl','num_bc_sats','num_bc_tl','num_il_tl','num_op_rev_tl','num_rev_accts','num_rev_tl_bal_gt_0','num_sats','num_tl_120dpd_2m','num_tl_30dpd','num_tl_90g_dpd_24m','num_tl_op_past_12m','pct_tl_nvr_dlq','percent_bc_gt_75','pub_rec_bankruptcies','tax_liens','tot_hi_cred_lim','total_bal_ex_mort','total_bc_limit','total_il_high_credit_limit']
    print("Adding file name and timestamp..")

    Df_required_Loan['file_name']='LoanStats3a'
    Df_required_Loan['time_stamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Df_required_Loan['Flag']= 1

    print(Df_required_Loan.head(2))
    
    #final_df = big_frame.append(Df_required_Loan,ignore_index=True)

    print('merging the two dataframe as one..')
    final_df1 = pd.concat([big_frame, Df_required_Loan], ignore_index=True)
    
    print("peek at first few rows of the dataframe..")


    # Creating a separate dataset from loans that don't meet credit policy
    
    Loan3a_not_meet_status_DF = Loan3aDf.ix[(Loan3aDf['loan_status']=='Does not meet the credit policy. Status:Charged Off') | (Loan3aDf['loan_status']=='Does not meet the credit policy. Status:Fully Paid')].values 
    Loan3aDf_not_meet_status = pd.DataFrame(Loan3a_not_meet_status_DF)
    Loan3aDf_not_meet_status.columns = ["id", "member_id", "loan_amnt", "funded_amnt",'funded_amnt_inv','term','int_rate','installment','grade','sub_grade','emp_title','emp_length','home_ownership','annual_inc','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','dti','delinq_2yrs','earliest_cr_line','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','initial_list_status','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d','last_pymnt_amnt','next_pymnt_d','last_credit_pull_d','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','application_type','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m','open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m','acc_open_past_24mths','avg_cur_bal','bc_open_to_buy','bc_util','chargeoff_within_12_mths','delinq_amnt','mo_sin_old_il_acct','mo_sin_old_rev_tl_op','mo_sin_rcnt_rev_tl_op','mo_sin_rcnt_tl','mort_acc','mths_since_recent_bc','mths_since_recent_bc_dlq','mths_since_recent_inq','mths_since_recent_revol_delinq','num_accts_ever_120_pd','num_actv_bc_tl','num_actv_rev_tl','num_bc_sats','num_bc_tl','num_il_tl','num_op_rev_tl','num_rev_accts','num_rev_tl_bal_gt_0','num_sats','num_tl_120dpd_2m','num_tl_30dpd','num_tl_90g_dpd_24m','num_tl_op_past_12m','pct_tl_nvr_dlq','percent_bc_gt_75','pub_rec_bankruptcies','tax_liens','tot_hi_cred_lim','total_bal_ex_mort','total_bc_limit','total_il_high_credit_limit']

    print("adding column names, file name and timestamp")
    Loan3aDf_not_meet_status['file_name']='LoanStats3a'
    Loan3aDf_not_meet_status['time_stamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Loan3aDf_not_meet_status['Flag']= 0

    print('merging the two dataframe as final merge..')
    DF_FINAL = pd.concat([final_df1, Loan3aDf_not_meet_status], ignore_index=True)

    print("peek at first few rows of the dataframe..")
    print(DF_FINAL.head())
    print("Saving the csv file")
    DF_FINAL.to_csv('Combined_data_file.csv',index=None)
    print("End of Script..")


# In[ ]:



