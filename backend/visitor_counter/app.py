import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

CORS_ORIGIN = 'https://sam-gardner.com'


def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='ADD #c :inc',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )

    count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': CORS_ORIGIN,
            'Access-Control-Allow-Methods': 'GET',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': count})
    }
