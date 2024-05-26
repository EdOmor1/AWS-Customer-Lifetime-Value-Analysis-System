# Customer-Lifetime-Value-Analysis-System

# Customer Lifetime Value (LTV) Analysis System

This project aims to build a system to track and analyze the lifetime value (LTV) of customers from mobile app campaigns across different regions.

## Objective

The objective of this system is to collect, store, process, analyze, and visualize data related to customer lifetime value using various AWS services.

## Project Structure

Customer-Lifetime-Value-Analysis-System
│
├── data_collection
│ └── kinesis_data_streams.py
│
├── data_storage
│ ├── s3_storage.py
│ └── aurora_db.py
│
├── data_processing
│ ├── lambda_processing.py
│ └── emr_processing.py
│
├── data_analytics
│ └── redshift_analytics.py
│
├── visualization
│ └── quicksight_visualization.py
│
├── infrastructure
│ ├── multi_az_setup.py
│ └── auto_scaling_setup.py
│
└── disaster_recovery
├── s3_replication.py
├── rds_multiaz.py
└── backup_setup.py


## Components and AWS Services

### Data Collection
- **Amazon Kinesis Data Streams**: Collects real-time data from mobile apps.

### Data Storage
- **Amazon S3**: Stores raw data for scalability and cost-effectiveness.
- **Amazon Aurora**: Stores structured relational data.

### Data Processing
- **AWS Lambda**: Processes data in real-time.
- **Amazon EMR**: Handles large-scale data processing and analysis.

### Data Analytics
- **Amazon Redshift**: Performs complex queries and analytics on large datasets.

### Visualization
- **Amazon QuickSight**: Visualizes LTV metrics and trends.

### High Availability
- **Multi-AZ Deployments**: Ensures high availability for databases and processing services.

### Scalability
- **Amazon Auto Scaling**: Automatically adjusts the number of EC2 instances based on load.

### Fault Tolerance
- **S3 Cross-Region Replication**: Ensures data is replicated across regions.
- **RDS Multi-AZ**: Provides fault tolerance for databases.

### Disaster Recovery
- **AWS Backup**: Automates backups of databases and ensures data recoverability in another region.

## How to Run

1. **Set up AWS Credentials**:
   Ensure you have the necessary AWS credentials configured. You can use the AWS CLI to configure your credentials:
   ```sh
   aws configure

Install Dependencies:
Install the necessary Python packages:
pip install boto3 pymysql

Run Data Collection:
Start collecting data from mobile apps:
python data_collection/kinesis_data_streams.py

Store Data:
Store raw data in S3 and structured data in Aurora:
python data_storage/s3_storage.py
python data_storage/aurora_db.py

Process Data:
Process data using AWS Lambda and Amazon EMR:
python data_processing/lambda_processing.py
python data_processing/emr_processing.py

Analyze Data:
Perform complex queries and analytics using Amazon Redshift:
python data_analytics/redshift_analytics.py

Visualize Data:
Visualize LTV metrics and trends using Amazon QuickSight:
python visualization/quicksight_visualization.py

Set up High Availability:
Ensure high availability for databases and processing services:
python infrastructure/multi_az_setup.py
python infrastructure/auto_scaling_setup.py

Set up Disaster Recovery:
Implement S3 cross-region replication and RDS Multi-AZ deployments:
python disaster_recovery/s3_replication.py
python disaster_recovery/rds_multiaz.py
python disaster_recovery/backup_setup.py

