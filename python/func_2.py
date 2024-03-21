import json
import boto3

dynamodb = boto3.resource('dynamodb')
hands_on_table = dynamodb.Table('testapi-dynamo-db')

def lambda_handler(event, context):
    
    id = event['queryStringParameters']['id']

    response = hands_on_table.get_item(
        Key={
            'id': id
        }
    )
    
    if 'Item' in response:
        return {
        'statusCode': 200,
        'body': json.dumps({
            'ID': response['Item']['id'],
            'Message': response['Item']['message'],
            'url': response['Item']['url'],
            'Lat': int(response['Item']['lat']),
            'Lon': int(response['Item']['lon']),
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