import json
import boto3

rds = boto3.client('rds')

def lambda_handler(event, context):
    
    id = event['queryStringParameters']['id']

    response = rds.describe_db_instances(
        DBInstanceIdentifier=id
    )
    
    if 'DBInstances' in response and response['DBInstances']:
        db_instance = response['DBInstances'][0]
        return {
        'statusCode': 200,
        'body': json.dumps({
            'ID': db_instance['DBInstanceIdentifier'],
            'Message': db_instance['DBInstanceStatus'],
            'url': db_instance['Endpoint']['Address'],
            'Lat': int(db_instance['AllocatedStorage']),
            'Lon': int(db_instance['BackupRetentionPeriod']),
        }),
        'isBase64Encoded': False,
        'headers':{}
    }
    else:
        return {
        'statusCode': 200,
        'body': json.dumps({
            'Message': "------404------- Not Found"
        }),
        'isBase64Encoded': False,
        'headers':{}
    }