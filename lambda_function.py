import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    instance = ec2.create_instances(
        ImageId='ami-0c2b8ca1dad447f8a',  # Replace with your region's AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='your-key-name',         # Replace with your key pair
        SecurityGroupIds=['sg-xxxxxxxx'],# Replace with your security group
        SubnetId='subnet-xxxxxxxx'       # Replace with your subnet
    )
    
    return {
        'statusCode': 200,
        'body': f"EC2 Instance Launched: {instance[0].id}"
    }
