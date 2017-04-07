
# coding: utf-8

# In[ ]:

# Filename: run_luigi.py
import luigi

import Declined_Validation as validate
import Declined_Merge_File as merge_file

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

    def run(self):
        print("running validate method..")
        validate.fill_empty_values()
    
                
if __name__ == '__main__':
    luigi.run(['Validate_Files','--local-scheduler'])

