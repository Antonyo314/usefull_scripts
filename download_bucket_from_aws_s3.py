import boto3
import os

zip_name = 'gtFine_trainvaltest.zip'

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
)

s3 = session.resource('s3')

bucket = s3.Bucket('latentai-ai-ml')
os.makedirs('downloads', exist_ok=True)
bucket.download_file(f'data/{zip_name}', f'downloads/{zip_name}')