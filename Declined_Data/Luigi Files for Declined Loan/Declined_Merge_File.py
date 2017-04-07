
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
import requests
import zipfile
from datetime import datetime
import io


# In[2]:

def download_declineddata():
    s = requests.session()
    years = ['A','B','D']

    for year in years:
        url3 = 'https://resources.lendingclub.com/RejectStats'+str(year)+'.csv.zip'
        file = s.get(url3)
        m=zipfile.ZipFile(io.BytesIO(file.content))
        m.extractall()
        
    years1 = [1,2,3,4]
    for year1 in years1:
        url3 = 'https://resources.lendingclub.com/RejectStats_2016Q'+str(year1)+'.csv.zip'
        file = s.get(url3)
        m=zipfile.ZipFile(io.BytesIO(file.content))
        m.extractall()
print('Declined Loan data files downloaded')


# In[3]:

def declinedata_merge():
    declinedloans_file = [file for file in os.listdir() if file.startswith('Reject')]
    df = pd.DataFrame()
    for i in range(len(declinedloans_file)):
        data = pd.read_csv(declinedloans_file[i],delimiter=',',skiprows=1)
        df = df.append(data)
        df['time_stamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.head(3)
    df.to_csv('CombinedRejectLoanStats.csv', index=None)
print('Files merged into a single file')


# In[ ]:




# In[ ]:



