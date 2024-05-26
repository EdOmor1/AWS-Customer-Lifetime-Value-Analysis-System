import boto3

# Initialize EMR client
emr = boto3.client('emr', region_name='your_region')

def run_emr_job():
    response = emr.run_job_flow(
        Name='LTV Analysis Job',
        LogUri='s3://your-log-uri',
        ReleaseLabel='emr-5.29.0',
        Instances={
            'InstanceGroups': [
                {
                    'Name': 'Master nodes',
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'MASTER',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 1,
                },
                {
                    'Name': 'Core nodes',
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'CORE',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 2,
                }
            ],
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
        },
        Steps=[
            {
                'Name': 'Calculate LTV',
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['spark-submit', 's3://your-spark-job-script']
                }
            }
        ],
        Applications=[
            {'Name': 'Spark'}
        ],
        Configurations=[
            {
                'Classification': 'spark',
                'Properties': {
                    'maximizeResourceAllocation': 'true'
                }
            }
        ],
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole'
    )
    print("EMR job started:", response['JobFlowId'])

if __name__ == "__main__":
    run_emr_job()
