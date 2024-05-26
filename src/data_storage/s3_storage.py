import boto3

# Initialize S3 client
s3 = boto3.client('s3', region_name='your_region')
bucket_name = 'your_bucket_name'

def upload_to_s3(file_name, object_name=None):
    try:
        response = s3.upload_file(file_name, bucket_name, object_name or file_name)
        print(f"File uploaded to S3: {file_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {str(e)}")

# Example usage
if __name__ == "__main__":
    upload_to_s3('local_file_path', 's3_object_name')
