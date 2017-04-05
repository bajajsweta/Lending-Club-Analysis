
# coding: utf-8

# In[1]:

# Filename: run_luigi.py
import luigi
import boto
from boto.s3.connection import S3Connection
from boto.s3.connection import Key

'''
class PrintNumbers(luigi.Task):
 
    def requires(self):
        return []
 
    def output(self):
        return luigi.LocalTarget("numbers_up_to_10.txt")
 
    def run(self):
        with self.output().open('w') as f:
            for i in range(1, 11):
                f.write("{}\n".format(i))
 
class SquaredNumbers(luigi.Task):
 
    def requires(self):
        return [PrintNumbers()]
 
    def output(self):
        return luigi.LocalTarget("squares.txt")
 
    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                out = n * n
                fout.write("{}:{}\n".format(n, out))
                '''

class UploadToS3(luigi.Task):
    #awsKey = luigi.Parameter(config_path=dict(section='path', names='aws_key'))
    #awsSecret = luigi.Parameter(config_path=dict(section='path', names='aws_secret'))
    awsKey = '*'
    awsSecret = '*'
    
    def requires(self):
        return []
    
    def output(self):
        
        #Create a connection
        access_key = self.awsKey
        #print(access_key)
        acess_secret = self.awsSecret
        conn = S3Connection(access_key,acess_secret)
        #print(conn)
        
        #Connecting to a bucket
        bucket_name = "luigibuckets"
        bucket = conn.get_bucket(bucket_name)
        #print(bucket)
        
        #Setting the keys
        k = Key(bucket)
        print (k)
        k.key = "squares.txt"
        k.set_contents_from_filename("squares.txt")

                 
if __name__ == '__main__':
    luigi.run(['UploadToS3','--local-scheduler'])


# In[ ]:




# In[ ]:



