import json
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProcessedData')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    lines = content.splitlines()
    record_count = len(lines) - 1

    table.put_item(
        Item={
            'id': key,
            'records': record_count
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully')
    }
