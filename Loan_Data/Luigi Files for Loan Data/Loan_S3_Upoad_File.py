
# coding: utf-8

# In[ ]:

import boto
from boto.s3.connection import S3Connection
from boto.s3.connection import Key


# In[ ]:

def uploadToS3():
    awsKey = 'AKIAJ4IZVFXNSFMLAU3A'
    awsSecret = '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'
    
    conn = S3Connection(awsKey,awsSecret)
        #print(conn)
        
        #Connecting to a bucket
    bucket_name = "luigibuckets"
    bucket = conn.get_bucket(bucket_name)
        #print(bucket)
        #Setting the keys
    k = Key(bucket)
    print (k)
    k.key = "LoanStats_Validated.csv"
    k.set_contents_from_filename("LoanStats_Validated.csv")


# In[ ]:



