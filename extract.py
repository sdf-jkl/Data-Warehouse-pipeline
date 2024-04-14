import boto3
import json
import requests

with open('keys.json') as f:
    keys = json.load(f)

dataset_link = 'https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD&api_foundry=true'

# URL of the CSV file
url = dataset_link

# S3 bucket and object key where you want to store the file
bucket_name = 'my-tf-test-bucket-meow-meow-meow'
object_key = 'nyc.csv'

# Download the file from the URL and upload it to S3
s3 = boto3.client('s3', aws_access_key_id = keys['access_key'], aws_secret_access_key = keys['secret_key'])
response = s3.put_object(Bucket=bucket_name, Key=object_key, Body=requests.get(url).content)

if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print(f"File '{object_key}' uploaded successfully to '{bucket_name}' bucket.")
else:
    print(f"Failed to upload file '{object_key}' to '{bucket_name}' bucket.")
