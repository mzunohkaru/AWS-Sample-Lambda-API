# PythonからAWSリソースとの連携
import boto3
import json
# JSONのアップロード
from collections import OrderedDict

def handler(event, context):
    
    BUCKET_NAME = event['bucket_name']
    BUCKET_KEY = event['bucket_key']
    UPLOAD_BUCKET_KEY = 'b.json'
    
    # a.jsonの読み込み
    s3Client = boto3.client('s3')
    obj = s3Client.get_object(Bucket=BUCKET_NAME, Key=BUCKET_KEY)
    data = json.loads(obj['Body'].read().decode('utf-8'))
    print(f'{BUCKET_KEY}の内容 : {data}')
    
    # b.jsonのアップロード
    s3Resource = boto3.resource('s3')
    obj = s3Resource.Bucket(BUCKET_NAME).Object(UPLOAD_BUCKET_KEY)
    data = OrderedDict(username=UPLOAD_BUCKET_KEY, point=data['point'] + 10, product=data['product'])
    
    res = obj.put(Body=json.dumps(data))
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f'[SUCCESS] upload {UPLOAD_BUCKET_KEY}')