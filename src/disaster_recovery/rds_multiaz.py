import boto3

# Initialize RDS client
rds = boto3.client('rds', region_name='your_region')

def setup_rds_multiaz():
    response = rds.modify_db_instance(
        DBInstanceIdentifier='your-db-instance-identifier',
        MultiAZ=True,
        ApplyImmediately=True
    )
    print("RDS Multi-AZ setup complete: ", response['DBInstance']['DBInstanceIdentifier'])

if __name__ == "__main__":
    setup_rds_multiaz()
