# This is a simple Demo for your reference to create IAM user, Set Tag for EC2 and create S3 bucket

# AWS python sdk (boto3) manual, please refer to 
# https://aws.amazon.com/sdk-for-python/
# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

# Important: Make sure you have setup AWS CLI and configure Access key for the machine you run this script at the first time
# If you don't know how to install AWS CLI, please refer to
# https://aws.amazon.com/cli/
# configure Access key command example: aws configure
# https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

# Please update your IAM Role Policy as example as iam_role_policy.json, and mark down and replace below PolicyArn
# Change region as you need
# Change the s3bucket_prefix as you need. Recommended to use a long name to avoid conflict.

import boto3

s3bucket_prefix = 'xxxxxcom-technology-' # set your s3 bucket prefix here
region = 'cn-northwest-1'  # Ningxia='cn-northwest-1', Beijing='cn-north-1'
PolicyArn = 'arn:aws-cn:iam::111000100010:policy/ec2-start-stop-on-tags-s3-access'

iam_user = input('Please input your IAM user name to create or input an exist IAM user: ')

# Check iam_user exist or create, attach policy
client_iam = boto3.client('iam')
try:
    response = client_iam.create_user(
        UserName=iam_user
    )
    response = client_iam.attach_user_policy(
        UserName=iam_user,
        PolicyArn=PolicyArn
        # Please replace the PolicyArn string as your IAM Role's ARN
    )
except Exception as e:
    print(e)


# TODO add python code to create EC2 here, so no need to ceate on Console
print('Please create your EC2 in Console within your prefer REGION and mark down Instance ID, such as i-0a1b2cd3e456fgh78 and input as below')

# Add Owner Tag for EC2 instances
ec2id_list=[]
ec2id='na'
while (ec2id!=''):
    ec2id=input('Please input EC2 instance id (empty enter to quit):')
    if ec2id != '':
        ec2id_list.append(ec2id)
print('Tag for EC2 instances: ', ec2id_list)

client_ec2 = boto3.client('ec2', region_name=region)
try:
    response = client_ec2.create_tags(
        Resources=ec2id_list,
        Tags=[
            {
                'Key': 'Owner',
                'Value': iam_user
            }
        ]
    )
except Exception as e:
    print(e)

# Create S3 bucket and Tag owner name
client_s3 = boto3.client('s3', region_name=region)
try:
    response = client_s3.create_bucket(
        Bucket=s3bucket_prefix+iam_user,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    response = client_s3.put_bucket_tagging(
        Bucket=s3bucket_prefix+iam_user,
        Tagging={
            'TagSet':[
                {
                    'Key': 'Owner',
                    'Value': iam_user
                }
            ]
        }
    )
    print('Successfully create S3 bucket and tag with owner: ',
          s3bucket_prefix+iam_user)
except Exception as e:
    print(e)
