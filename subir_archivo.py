import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']
    nombre_archivo = body['nombre']
    contenido = base64.b64decode(body['contenido'])

    key = f"{directorio}/{nombre_archivo}"
    s3.put_object(Bucket=bucket, Key=key, Body=contenido)
    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f"Archivo '{nombre_archivo}' subido a {key}"})
    }
