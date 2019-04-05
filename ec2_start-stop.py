#!/usr/bin/env python

import sys
import boto3

ec2client = boto3.client('ec2')
ec2details = ec2client.describe_instances()


a=[]
b=[]
c=[]

for i in ec2details['Reservations']:
    for ii in (i['Instances']):
        a.append((ii["InstanceId"]))
        b.append(ii["State"]["Code"])
        c.append(ii["State"]["Name"])

for i in range(len(a)):
    if b[i] == 16:
        ec2client.stop_instances(InstanceIds=a, DryRun=False)
        print('The instance '+a[i]+' is stopped')
    elif b[i] == 80:
        ec2client.start_instances(InstanceIds=a, DryRun=False)
        print('The instance '+a[i]+' is started')
    else:
        print('The instance '+a[i]+' is '+c[i])
