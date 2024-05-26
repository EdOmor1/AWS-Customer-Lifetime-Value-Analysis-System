import boto3

# Initialize Auto Scaling client
autoscaling = boto3.client('autoscaling', region_name='your_region')

def setup_auto_scaling():
    response = autoscaling.create_auto_scaling_group(
        AutoScalingGroupName='your-asg-name',
        InstanceId='your-instance-id',
        MinSize=1,
        MaxSize=5,
        DesiredCapacity=2,
        AvailabilityZones=[
            'us-west-2a',
            'us-west-2b'
        ]
    )
    print("Auto Scaling group created: ", response)

if __name__ == "__main__":
    setup_auto_scaling()
