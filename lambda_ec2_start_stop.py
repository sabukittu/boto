## Lambda Function to Start and Stop Ec2 Instance ##

import os
import boto3
import json

ec2client = boto3.client('ec2')
ec2details = ec2client.describe_instances()

a=[]
b=[]
c=[]

def ec2_start_stop():

    for i in ec2details['Reservations']:
        for ii in (i['Instances']):
            a.append((ii["InstanceId"]))
            b.append(ii["State"]["Code"])
            c.append(ii["State"]["Name"])

    for i in range(len(a)):
        if b[i] == 16:
            ec2stop = ec2client.stop_instances(InstanceIds=a, DryRun=False)
            return ec2stop
        elif b[i] == 80:
            ec2start = ec2client.start_instances(InstanceIds=a, DryRun=False)
            return ec2start


def lambda_handler(event, context):
    if(event.get('action') == 'start'):
        response = ec2_start_stop()
    if(event.get('action') == 'stop'):
        response = ec2_start_stop()
    return response