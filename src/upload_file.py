import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT_URL"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

BUCKET_NAME = "raw-data"
OBJECT_KEY = "sales/2024/01/data.csv"

csv_content = """date,region,sales
2024-01-01,us-east,1200.00
2024-01-02,us-west,980.50
2024-01-03,eu-west,1540.00
"""

try:
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=OBJECT_KEY,
        Body=csv_content,
        ContentType="text/csv",
    )

    print(f"Uploaded '{OBJECT_KEY}' to bucket '{BUCKET_NAME}'.")

except ClientError as error:
    print(f"Upload failed: {error}")