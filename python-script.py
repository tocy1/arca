# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import boto3.ec2
import sys
from botocore.exceptions import ClientError
'''
You must create your credential file yourself. By default, its location is at ~/.aws/credentials:

[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
You must also set a default region. This can be done in the configuration file. By default, its location is at ~/.aws/config:

[default]
region=us-east-1
'''
class awsStartStopInstance():
    def main(self):
        # read arguments from the command line and 
        # check whether at least two elements were entered
        if len(sys.argv) < 3:
        	print("Usage: python python-script.py {start|stop} <instance_id>\n")
        	sys.exit(0)
        else:
            action = sys.argv[1]
        if action == "start":
            self.startInstance(sys.argv[2])
        elif action == "stop":
        	self.stopInstance(sys.argv[2])
        else:
        	print("Usage: python aws.py {start|stop} <instance_id>\n")
    def startInstance(self,instance_id):
        print("Starting the instance...")
        ec2=boto3.client('ec2')
        try:
             ec2.start_instances(instance_ids=[instance_id],DryRun=False)
    
        except ClientError as err:
            error2 = "Error2: {0}".format(err)
            print(error2)
            sys.exit(0)
    
    def stopInstance(self,instance_id):
        print("Stopping the instance...")
        ec2=boto3.client('ec2')
        try:
             ec2.stop_instances(instance_ids=[instance_id],DryRun=False)
    
        except ClientError as err:
            error2 = "Error2: {0}".format(err)
            print(error2)
            sys.exit(0)

if __name__ == '__main__':
    aws=awsStartStopInstance()
    aws.main()
