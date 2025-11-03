import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = event['body']
    bucket_name = body['bucket']
    s3.create_bucket(Bucket=bucket_name)
    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f"Bucket '{bucket_name}' creado correctamente"})
    }
