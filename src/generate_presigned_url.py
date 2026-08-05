import os
import urllib.request
import boto3
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# S3 client configuration
boto_kwargs = dict(
    endpoint_url=os.getenv("S3_ENDPOINT_URL", "http://localhost:4566"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

s3 = boto3.client("s3", **boto_kwargs)

bucket_name = "raw-data"
object_key = "sales/2024/01/data.csv"

# Create bucket if it does not exist
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Created bucket: {bucket_name}")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket already exists: {bucket_name}")

# Upload sample object
s3.put_object(
    Bucket=bucket_name,
    Key=object_key,
    Body=b"date,region,sales\n2024-01-01,us-east,1200.00\n",
)

print(f"Uploaded object: {object_key}")

# Generate a pre-signed URL valid for 60 seconds
url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": bucket_name,
        "Key": object_key,
    },
    ExpiresIn=60,
)

print("\nPre-signed URL:")
print(url)

# Access object using URL without AWS credentials
with urllib.request.urlopen(url) as response:
    print("\nContent:")
    print(response.read().decode())