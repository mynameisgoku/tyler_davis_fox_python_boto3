#Code Test

#Using the AWS Python SDK Boto3 (https://aws.amazon.com/sdk-for-python/), build a python script (or multiple scripts) that does the following things:

#1. creates a private S3 bucket in the us-west-2 region  
#2. uploads a file in the newly created bucket that is a list of all buckets in the account.  











import boto3
import os
import uuid #will need to run multiple times; may use uuid for unique bucket names
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
#https://docs.python.org/3/library/uuid.html#module-uuid
#https://www.geeksforgeeks.org/python-os-path-exists-method/
#https://www.geeksforgeeks.org/python-os-remove-method/

s3_client = boto3.client('s3', region_name='us-west-2')
bucketName = 'tyler-'+str(uuid.uuid1())
bucket = s3_client.create_bucket(ACL='private',Bucket=bucketName,
        CreateBucketConfiguration={'LocationConstraint': 'us-west-2'} )


if os.path.exists("s3_list.txt"):
  os.remove("s3_list.txt")
else:
  print("The file does not exist")
f = open("s3_list.txt", "w")
s3_resource = boto3.resource('s3')
for bucket in s3_resource.buckets.all():
   # print (bucket.name)
# https://www.w3schools.com/python/python_file_write.asp
    f = open("s3_list.txt", "a")
    f.write(bucket.name + '\n')
    f.close()

#2. uploads a file in the newly created bucket that is a list of all buckets in the account. 
#https://stackoverflow.com/questions/37017244/uploading-a-file-to-a-s3-bucket-with-a-prefix-using-boto3
s3_resource.meta.client.upload_file('s3_list.txt', bucketName, 's3_list.txt')
