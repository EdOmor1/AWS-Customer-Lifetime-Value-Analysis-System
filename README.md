# Customer Lifetime Value (LTV) Analysis System

This project aims to build a system to track and analyze the lifetime value (LTV) of customers from mobile app campaigns across different regions.

## Objective

The objective of this system is to collect, store, process, analyze, and visualize data related to customer lifetime value using various AWS services.

## Project Structure

- src: Contains the source code for different components.
   - data_collection: Scripts for collecting real-time data from mobile apps using Amazon Kinesis Data Streams.
   - kinesis_data_streams.py: Script to set up and manage data streams for real-time data collection.
   - data_storage: Scripts for storing raw and structured data.
      - s3_storage.py: Script for storing raw data in Amazon S3.
      - aurora_db.py: Script for storing structured relational data in Amazon Aurora (MySQL compatible).
   - data_processing: Scripts for processing data using AWS Lambda and Amazon EMR.
      - lambda_processing.py: AWS Lambda function script for real-time data processing.
      - emr_processing.py: Script for processing large-scale data using Amazon EMR.
   - data_analytics: Scripts for performing complex queries and analytics.
      - redshift_analytics.py: Script for running analytics and complex queries on large datasets using Amazon Redshift.
   - visualization: Scripts for visualizing data.
      - quicksight_visualization.py: Script for creating visualizations and dashboards using Amazon QuickSight.
   - infrastructure: Scripts to set up AWS infrastructure components to ensure high availability, scalability, and fault tolerance.
      - multi_az_setup.py: Script to configure Multi-AZ deployments for high availability.
      - auto_scaling_setup.py: Script to set up Amazon Auto Scaling for automatic scaling of EC2 instances.
   - disaster_recovery: Scripts for implementing disaster recovery mechanisms.
      - s3_replication.py: Script to set up S3 cross-region replication for fault tolerance.
      - rds_multiaz.py: Script to configure RDS Multi-AZ deployments for fault-tolerant databases.
      - backup_setup.py: Script to set up AWS Backup for automated backups and disaster recovery.

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

2. **Install Dependencies**:
Install the necessary Python packages:
 ```sh
pip install boto3 pymysql

3. **Run Data Collection**:
Start collecting data from mobile apps:
 ```sh
python data_collection/kinesis_data_streams.py

4. **Store Data**:
Store raw data in S3 and structured data in Aurora:
 ```sh
python data_storage/s3_storage.py
python data_storage/aurora_db.py

5. **Process Data**:
 ```sh
Process data using AWS Lambda and Amazon EMR:
python data_processing/lambda_processing.py
python data_processing/emr_processing.py

6. **Analyze Data**:
 ```sh
Perform complex queries and analytics using Amazon Redshift:
python data_analytics/redshift_analytics.py

7. **Visualize Data**:
Visualize LTV metrics and trends using Amazon QuickSight:
 ```sh
python visualization/quicksight_visualization.py

8. **Set up High Availability**:
Ensure high availability for databases and processing services:
 ```sh
python infrastructure/multi_az_setup.py
python infrastructure/auto_scaling_setup.py

9. **Set up Disaster Recovery**:
Implement S3 cross-region replication and RDS Multi-AZ deployments:
 ```sh
python disaster_recovery/s3_replication.py
python disaster_recovery/rds_multiaz.py
python disaster_recovery/backup_setup.py

