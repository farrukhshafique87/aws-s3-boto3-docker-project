# Generate and Access an S3 Pre-Signed URL

## Overview

This script demonstrates how to create an S3 bucket, upload an object, generate a pre-signed URL, and access the object without AWS credentials.

The project uses **Floci** as a local AWS environment, so all S3 operations are performed against the local endpoint instead of real AWS.

## What This Script Does

The script performs the following steps:

1. Loads AWS configuration from environment variables.
2. Creates an S3 client connected to Floci.
3. Creates an S3 bucket named `raw-data`.
4. Uploads a sample CSV file.
5. Generates a pre-signed URL that allows temporary access to the object.
6. Downloads the object using the URL without providing AWS credentials.

## Configuration

The script expects these environment variables:

```env
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_DEFAULT_REGION=us-east-1
S3_ENDPOINT_URL=http://localhost:4566
```

For Floci, the credentials are dummy values because the service runs locally.

## S3 Resources Created

### Bucket

```
raw-data
```

### Object

```
sales/2024/01/data.csv
```

The uploaded file contains:

```csv
date,region,sales
2024-01-01,us-east,1200.00
```

## Running the Script

Make sure Floci is running:

```bash
floci status
```

Run the script:

```bash
python3 presigned_url.py
```

## Expected Output

Example:

```
Created bucket: raw-data
Uploaded object: sales/2024/01/data.csv

Pre-signed URL:
http://localhost:4566/raw-data/sales/2024/01/data.csv?...signature...

Content:
date,region,sales
2024-01-01,us-east,1200.00
```

## How Pre-Signed URLs Work

A pre-signed URL provides temporary access to an S3 object without requiring the user to have AWS credentials.

The URL contains:

* Bucket name
* Object key
* Expiration time
* AWS signature

Anyone with the URL can access the object until it expires.

In this script:

```python
ExpiresIn=60
```

means the generated URL is valid for **60 seconds**.

## Use Cases

Pre-signed URLs are commonly used for:

* Allowing users to download private files
* Uploading files directly to S3 from applications
* Sharing temporary access to objects
* Avoiding exposure of AWS credentials

## Notes for Floci

This project runs against:

```
http://localhost:4566
```

instead of the AWS S3 service endpoint.

The same code pattern works with real AWS S3 by replacing the endpoint URL and using valid AWS credentials.
