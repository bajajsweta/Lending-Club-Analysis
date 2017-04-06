
# coding: utf-8

# In[6]:

import urllib
import os
import sys
import requests
import pandas as pd
import zipfile
import io


# In[7]:

def download_data():
    print("Scraping data from lending club website.")
    s = requests.session()
    letters = 'abcd'
    for each in letters:
        url = 'https://resources.lendingclub.com/LoanStats3'+each+'.csv.zip'
        file1 = s.get(url)
        m1 = zipfile.ZipFile(io.BytesIO(file1.content))
        m1.extractall()
        print("File"+'LoanStats3'+each+'is downloaded..!')
    Quarter = ['Q1','Q2','Q3','Q4']
    for q in Quarter:
        url = 'https://resources.lendingclub.com/LoanStats_2016'+q+'.csv.zip'
        file = s.get(url)
        m = zipfile.ZipFile(io.BytesIO(file.content))
        m.extractall()
        #download= urllib.request.urlretrieve(url,'LoanStats_2016'+q+'.csv.zip')
        print("File"+'LoanStats_2016'+q+'is downloaded..!')
print("Downloading of csv files is completed..")


# In[8]:

#download_data()


# In[ ]:



