import boto3

# Initialize S3 client
s3 = boto3.client('s3', region_name='your_region')

def setup_s3_replication():
    replication_configuration = {
        'Role': 'arn:aws:iam::your_aws_account_id:role/your-role',
        'Rules': [
            {
                'Status': 'Enabled',
                'Priority': 1,
                'Filter': {
                    'Prefix': ''
                },
                'Destination': {
                    'Bucket': 'arn:aws:s3:::your-destination-bucket'
                }
            }
        ]
    }
    
    response = s3.put_bucket_replication(
        Bucket='your-source-bucket',
        ReplicationConfiguration=replication_configuration
    )
    print("S3 replication setup complete: ", response)

if __name__ == "__main__":
    setup_s3_replication()
