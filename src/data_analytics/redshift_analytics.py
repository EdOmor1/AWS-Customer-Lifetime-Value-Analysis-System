import boto3

# Initialize Redshift client
redshift = boto3.client('redshift', region_name='your_region')

def query_redshift():
    client = boto3.client('redshift-data', region_name='your_region')
    response = client.execute_statement(
        ClusterIdentifier='your-cluster-identifier',
        Database='your-database',
        DbUser='your-db-user',
        Sql='SELECT * FROM ltv_data;'
    )
    print("Query executed: ", response['Id'])

if __name__ == "__main__":
    query_redshift()
