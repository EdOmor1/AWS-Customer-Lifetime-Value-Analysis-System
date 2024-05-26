import boto3

# Initialize QuickSight client
quicksight = boto3.client('quicksight', region_name='your_region')

def create_analysis():
    response = quicksight.create_analysis(
        AwsAccountId='your_aws_account_id',
        AnalysisId='ltv-analysis',
        Name='LTV Analysis',
        SourceEntity={
            'SourceTemplate': {
                'DataSetReferences': [
                    {
                        'DataSetArn': 'arn:aws:quicksight:your_region:your_aws_account_id:dataset/your_dataset_id',
                        'DataSetPlaceholder': 'ltv_dataset'
                    }
                ],
                'Arn': 'arn:aws:quicksight:your_region:your_aws_account_id:template/your_template_id'
            }
        },
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:your_region:your_aws_account_id:user/default/your_user_name',
                'Actions': [
                    'quicksight:RestoreAnalysis',
                    'quicksight:UpdateAnalysisPermissions'
                ]
            }
        ]
    )
    print("QuickSight analysis created: ", response['Arn'])

if __name__ == "__main__":
    create_analysis()
