import json
import boto3
print('Loading function')
ec2 = boto3.client('ec2')


def getEc2List():
    ec2List = []
    response_instance = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag-key',
                'Values': [
                    'autostart',
                ]
            },
        ]
    )
    if response_instance['Reservations'] != []:
        for j in response_instance['Reservations']:
            for k in j['Instances']:
                ec2List.append(k['InstanceId'])
    return ec2List


def startEC2(ec2List):
    try:
        ec2.start_instances(
            InstanceIds=ec2List
        )
    except Exception as e:
        print(e)
    print('start EC2', ec2List)
    return


def stopEC2(ec2List):
    try:
        ec2.stop_instances(
            InstanceIds=ec2List
        )
    except Exception as e:
        print(e)
    print('stop EC2', ec2List)
    return


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    ec2List = getEc2List()
    if event['cronaction'] == 'start':
        startEC2(ec2List)
    if event['cronaction'] == 'stop':
        stopEC2(ec2List)

    return
