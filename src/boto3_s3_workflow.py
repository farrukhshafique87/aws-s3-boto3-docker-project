import boto3

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test',
)

# Create a bucket
s3.create_bucket(Bucket='demo')

# Upload several objects
for month in ['01', '02', '03']:
    s3.put_object(
        Bucket='demo',
        Key='reports/2024/' + month + '/summary.txt',
        Body=('Month ' + month + ' report').encode(),
        ContentType='text/plain',
    )

# List with a prefix filter
resp = s3.list_objects_v2(Bucket='demo', Prefix='reports/2024/')
print('Objects:')
for obj in resp.get('Contents', []):
    print('  ' + obj['Key'] + '  (' + str(obj['Size']) + ' bytes)')

# Download one
data = s3.get_object(Bucket='demo', Key='reports/2024/01/summary.txt')
print('\nContent of 01/summary.txt:')
print(data['Body'].read().decode())