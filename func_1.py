import json
import boto3
import datetime

client = boto3.client('translate')

dynamodb = boto3.resource('dynamodb')
hands_on_table = dynamodb.Table('hands-on-dynamo-db')

def lambda_handler(event, context):
    
    input_text = event['queryStringParameters']['input_text']
    
    response = client.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en',
    )
    
    output_text = response.get('TranslatedText')
    
    hands_on_table.put_item(
        Item = {
            'timestamp': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            'input_text': input_text,
            'output_text': output_text
        }
    )
    

    return {
        'statusCode': 200,
        'body': json.dumps({
            'Out Put': output_text
        }),
        'isBase64Encoded': False,
        'headers':{}
    }