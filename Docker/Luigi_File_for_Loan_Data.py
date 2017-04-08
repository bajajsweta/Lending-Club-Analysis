
# coding: utf-8

# In[1]:



# In[7]:+

# Filename: run_luigi.py
import luigi
import Validation_Script as validate
import Merging_The_file_To_one_Dataset as merge_file
import Loan_S3_Upoad_File as s3
import time

class Download_files(luigi.Task):
     
    def requires(self):
        return []
    
    def output(self):
        return luigi.LocalTarget("Combined_data_file.csv")
    
    def run(self):
        merge_file.download_data()
        merge_file.reading_files_to_merge()

        
class Validate_Files(luigi.Task):
     
    def requires(self):
        return [Download_files()]

    def output(self):
        return luigi.LocalTarget("LoanStats_Validated.csv")

	
	#def output(self):
		#return luigi.LocalTarget("LoanStats_Validated.csv")

    def run(self):
        print("running validate method..")
        validate.validate_field()
        validate.feature_engineering()
        

class UploadToS3(luigi.Task):
    #awsKey = luigi.Parameter(config_path=dict(section='path', names='aws_key'))
    #awsSecret = luigi.Parameter(config_path=dict(section='path', names='aws_secret'))
    def requires(self):
        time.sleep(40)
        return [Validate_Files()]

    def run(self):
        print("running validate method..")
        s3.uploadToS3()

                
if __name__ == '__main__':
    luigi.run(['UploadToS3','--local-scheduler'])






# In[ ]:



