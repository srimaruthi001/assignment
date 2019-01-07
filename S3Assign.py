import boto3
from boto3 import client
s3=boto3.resource('s3')
resp=client('s3')
s3.meta.client.upload_file('file_path/Assignment.txt','wiproinpimages','assgnmt.txt')
for obj in resp.list_objects(Bucet='wiproinpimages')['Contents']:
    print(obj['Key'])
