import boto3
import tempfile
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        with tempfile.NamedTemporaryFile() as tmp:
            s3.download_file(bucket, key, tmp.name)
            
            # Process image
            with Image.open(tmp.name) as img:
                img = img.convert('RGB')
                img.thumbnail((1200, 1200))
                webp_path = f"{tmp.name}.webp"
                img.save(webp_path, 'WEBP', quality=85)
                
            s3.upload_file(webp_path, bucket, f"processed/{key.split('.')[0]}.webp")
    
    return {"statusCode": 200} 