
# coding: utf-8

# In[7]:

# Filename: run_luigi.py
import luigi

import Validation_Script as validate
import Merging_The_file_To_one_Dataset as merge_file

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

    def run(self):
        print("running validate method..")
        validate.validate_field()
    
                
if __name__ == '__main__':
    luigi.run(['Validate_Files','--local-scheduler'])


# In[ ]:




# In[ ]:



