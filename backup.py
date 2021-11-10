#!/usr/bin/env python3

import boto3
import os
import sys
from datetime import datetime

localDir = sys.argv[1]
bucketName, cloudDir = sys.argv[2].split("::")

s3 = boto3.client('s3')
objects = ""

my_session = boto3.session.Session()
my_region = my_session.region_name

try: 
	objects = s3.list_objects(Bucket=bucketName)
except Exception as e:
	print("The bucket you gave does not exist, It is currently being created in the", my_region, "region.")
	try:
		s3.create_bucket(Bucket=bucketName, CreateBucketConfiguration={
        	'LocationConstraint': my_region
    	})
	except Exception as e:
		print("The bucket you gave has a name conflict with something else in your AWS account.")
		sys.exit()

#get all paths that exist in s3 and their lastmodified date as well.
h = {}
if "Contents" in objects:
	for o in objects["Contents"]:
		h[o['Key']] = o['LastModified']


#for every file in the directory specified, check if its already in s3 and up to date in the cloudPath provided. If not then reupload it to that cloudPath
for root, dirs, files in os.walk(localDir, topdown = False):
	for name in files:
		localPath = os.path.join(root, name)
		key = localPath.split('/')[1:]
		date = datetime.utcfromtimestamp(os.path.getmtime(localPath))
		cloudPath = cloudDir + '/'
		for x in key:
			cloudPath += x + '/'	
		cloudPath = cloudPath[:-1]
		uploadFile = False
		if cloudPath in h:
			if h[cloudPath].replace(tzinfo=None) < date.replace(tzinfo=None):
				uploadFile = True
		else:
			uploadFile = True

		if uploadFile:
			print('uploading file with path:', localPath, 'to s3.')
			os.utime(localPath, None)
			s3.upload_file(localPath, bucketName, cloudPath)
		else:
			print('file:', localPath, 'already uploaded to s3.')	
	

