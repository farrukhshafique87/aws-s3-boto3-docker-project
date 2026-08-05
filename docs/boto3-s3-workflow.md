# Boto3 S3 Workflow

## Overview

This example demonstrates a complete S3 workflow using the Python `boto3` SDK with a local AWS environment powered by Floci.

The workflow covers:

1. Creating an S3 bucket
2. Uploading multiple objects using structured object keys
3. Listing objects using a prefix filter
4. Downloading and reading an object

This demonstrates common S3 patterns used in real-world applications, such as organizing objects using prefixes and retrieving specific files from object storage.

## Configuration

The script connects to Floci instead of AWS:

```python
endpoint_url='http://localhost:4566'
```

The credentials are local development credentials:

```python
aws_access_key_id='test'
aws_secret_access_key='test'
```

Configuration:

```text
Endpoint: http://localhost:4566
Region: us-east-1
Access Key: test
Secret Key: test
```

## Creating an S3 Bucket

The script creates a bucket named:

```text
demo
```

Using boto3:

```python
s3.create_bucket(Bucket='demo')
```

This bucket will store report objects.

## Uploading Multiple Objects

The script uploads three monthly reports:

```text
reports/2024/01/summary.txt
reports/2024/02/summary.txt
reports/2024/03/summary.txt
```

The object key structure uses prefixes:

```text
reports/
└── 2024/
    ├── 01/
    │   └── summary.txt
    ├── 02/
    │   └── summary.txt
    └── 03/
        └── summary.txt
```

S3 does not use real folders. These paths are object key names that allow objects to be logically grouped.

## Listing Objects Using Prefix Filtering

The script uses:

```python
s3.list_objects_v2(
    Bucket='demo',
    Prefix='reports/2024/'
)
```

The prefix filter returns only objects that begin with:

```text
reports/2024/
```

Example output:

```text
Objects:
  reports/2024/01/summary.txt  (18 bytes)
  reports/2024/02/summary.txt  (18 bytes)
  reports/2024/03/summary.txt  (18 bytes)
```

Prefix filtering is commonly used to:

* Retrieve objects by category
* Process data partitions
* Organize logs and reports
* Implement data pipelines

## Downloading an Object

The script downloads:

```text
reports/2024/01/summary.txt
```

Using:

```python
s3.get_object(
    Bucket='demo',
    Key='reports/2024/01/summary.txt'
)
```

The object content is read from the response body:

```python
data['Body'].read().decode()
```

Example output:

```text
Content of 01/summary.txt:
Month 01 report
```

## Running the Example

Ensure Floci is running:

```bash
floci status
```

Run the script:

```bash
python3 boto3_s3_workflow.py
```

## Key S3 Concepts Demonstrated

### Buckets

Buckets are top-level containers used to store objects.

Example:

```text
demo
```

### Objects

Objects contain:

* Key name
* Data
* Metadata

Example:

```text
reports/2024/01/summary.txt
```

### Object Keys

S3 object keys provide a way to organize objects using naming conventions.

Example:

```text
reports/2024/01/summary.txt
```

### Prefix Queries

Prefixes allow applications to retrieve groups of objects without listing the entire bucket.

Example:

```text
Prefix: reports/2024/
```

## Real AWS Usage

The same boto3 workflow applies to Amazon S3 by changing:

```python
endpoint_url='http://localhost:4566'
```

to the standard AWS S3 endpoint and using valid AWS credentials.

This pattern is commonly used for:

* Data lake storage
* Report generation systems
* Backup workflows
* ETL pipelines
* Application file storage
