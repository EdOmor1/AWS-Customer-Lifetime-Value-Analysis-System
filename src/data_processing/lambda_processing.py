import json
import boto3

# Initialize the client
client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        # Get the message body
        payload = record["body"]
        data = json.loads(payload)
        # Process the data here
        print("Received data: ", data)
    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed')
    }
