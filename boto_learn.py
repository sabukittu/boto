#!/Users/kittusabu/Documents/boto_learn/venv/bin/python


import boto3

ec2client = boto3.client('ec2')
ec2details = ec2client.describe_instances()


a=[]
b=[]
for i in ec2details['Reservations']:
        for ii in (i['Instances']):
                a.append((ii["InstanceId"]))
                b.append(ii["State"]["Name"])



for i in range(len(a)):
        if b[i] == 'running':
                print('The instance '+a[i]+' is '+b[i])
        else:
                print('The instance '+a[i]+' is '+b[i])

