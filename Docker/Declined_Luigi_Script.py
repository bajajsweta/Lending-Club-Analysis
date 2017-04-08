
# coding: utf-8

# In[1]:

# Filename: run_luigi.py
import luigi

import Declined_Validation as validate
import Declined_Merge_File as merge_file
import Declined_Loan_S3_Upoad_File as s3
import time



class Download_files(luigi.Task):
     
    def requires(self):
        return []

    
    def output(self):
        return luigi.LocalTarget("CombinedRejectLoanStats.csv")
    
    def run(self):
        merge_file.download_declineddata()
        merge_file.declinedata_merge()
        
class Validate_Files(luigi.Task):
     
    def requires(self):
        return [Download_files()]
    
    def output(self):
        return luigi.LocalTarget("ValidatedCombinedRejectLoan.csv")

    def run(self):
        print("running validate method..")
        validate.fill_empty_values()
        
    

class UploadToS3(luigi.Task):
    #awsKey = luigi.Parameter(config_path=dict(section='path', names='aws_key'))
    #awsSecret = luigi.Parameter(config_path=dict(section='path', names='aws_secret'))
    def requires(self):
        time.sleep(20)
        return [Validate_Files()]

    def run(self):
        print("running validate method..")
        s3.uploadToS3()
        
      
        

    
                
if __name__ == '__main__':
    luigi.run(['UploadToS3','--local-scheduler'])


# In[ ]:



