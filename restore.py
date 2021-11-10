#!/usr/bin/env python3

import boto3
import os
import sys
from datetime import datetime

bucketName, cloudDir = sys.argv[1].split("::")
localDir = sys.argv[2]

s3 = boto3.resource('s3')
my_bucket = s3.Bucket(bucketName)

for obj in my_bucket.objects.filter(Prefix=cloudDir+'/'):
	x = obj.key.split('/')[1:]
	path = ""
	for val in x:
		path += val + '/'	
	path = path[:-1]

	localPath = localDir+'/'+path
	y = localPath.split('/')[:-1]
	directoriesMaker = ""
	for val in y:
		directoriesMaker += val + '/'
	isExist = os.path.exists(directoriesMaker)
	print('making these directories: ', directoriesMaker)
	if ~isExist:
		try:
			os.makedirs(directoriesMaker)
		except Exception as e:
			pass
			
	
	print('cloud download: ', obj.key)
	print('local to: ', localPath)
		
	my_bucket.download_file(obj.key, localPath)

	




