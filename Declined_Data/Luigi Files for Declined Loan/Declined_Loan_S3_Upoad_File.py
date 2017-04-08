
# coding: utf-8

# In[1]:

import boto
from boto.s3.connection import S3Connection
from boto.s3.connection import Key


# In[7]:

def uploadToS3():
	aKey = input("Enter the Key:")
    aSKey = input("Enter the Secret Key:")
    
    
    awsKey = aKey 
    awsSecret = aSKey '
    
    conn = S3Connection(awsKey,awsSecret)
        #print(conn)
        
        #Connecting to a bucket
    bucket_name = "luigibuckets"
    bucket = conn.get_bucket(bucket_name)
        #print(bucket)
        #Setting the keys
    k = Key(bucket)
    print (k)
    k.key = "ValidatedCombinedRejectLoan.csv"
    k.set_contents_from_filename("ValidatedCombinedRejectLoan.csv")


# In[ ]:



