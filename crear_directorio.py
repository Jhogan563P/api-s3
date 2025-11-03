import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']
    s3.put_object(Bucket=bucket, Key=f"{directorio}/")
    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f"Directorio '{directorio}' creado en {bucket}"})
    }
