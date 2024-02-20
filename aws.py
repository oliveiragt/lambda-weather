import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_file_path, bucket_name, s3_file_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(local_file_path, bucket_name, s3_file_name, ExtraArgs={'ContentType': 'text/html', 'ACL': 'public-read'})
        print(f"File {local_file_path} uploaded to {bucket_name}/{s3_file_name}")

    except FileNotFoundError:
        print(f"The file {local_file_path} was not found")

    except NoCredentialsError:
        print("Credentials not available")


