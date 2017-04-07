
# coding: utf-8

# In[1]:



# In[7]:+

# Filename: run_luigi.py
import luigi
import Validation_Script as validate
import Merging_The_file_To_one_Dataset as merge_file
import Feature_Engineering_Loans_File as feature_file
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
        time.sleep(20)
        return [Download_files()]
    
    def output(self):
        return luigi.LocalTarget("LoanStats_Validated.csv")

    def run(self):
        print("running validate method..")
        time.sleep(20)
        validate.validate_field()
        
class Feature_Engg_Files(luigi.Task):
     
    def requires(self):
        time.sleep(20)
        return [Validate_Files()]
    
    def output(self):
        return luigi.LocalTarget("LoanStats_Featured.csv")
    

    def run(self):
        print("running feature Engineering method..")
        feature_file.feature_engineering()
    
                
if __name__ == '__main__':
    luigi.run(['Feature_Engg_Files','--local-scheduler'])






# In[ ]:



