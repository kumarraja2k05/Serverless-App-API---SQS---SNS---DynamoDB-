import json
import os
import boto3

QUEUE_ARN = os.getenv("SQSQueue")

sqs_client = boto3.client("sqs", "us-west-2")

def lambda_handler(event, context):
    print("event body: ",event.get("Records")[0].get("body"))
    print("ARN: ",QUEUE_ARN)
    sqs_response = sqs_client.receive_message(
        QueueUrl = QUEUE_ARN,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    print("\nsqs response: ",sqs_response)
    return {
        "statusCode": 200,
        "body": "Hello New Function!!"
    }