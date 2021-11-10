#BackUpAndRestoreOnAWS

Purpose:

This project was an assignment for my Cloud Computing Class. The goal of this project was to create two python scripts. One script that can backup all the files in a directory to the cloud, and one that can restore a directory from the cloud onto your local computer. Folder and file structure is maintained on S3.

How To:

To execute a backup:
	./backup.py LocalDirectory BucketName::CloudDirectory
An example of this is:
	./backup.py localDir cs436-p3::cloudDir
	in this example
		localDir = localDirectory
		cs436-p3 = BucketName
		cloudDir = CloudDirectory
This is basically taking everything that is in the LocalDirectory and uploading it to s3 inside the CloudDirectory.

exceptions:
	If no cloud directory is provided, files will go under a directory called '/'.

To execute a restore:
	./restore.py BucketName::CloudDirectory LocalDirectory
An example of this is:
	./restore.py cs436-p3::cloudDir newDirectory
	in this example
		cs436-p3 = BucketName
		cloudDir = CloudDirectory
		newDirectory = LocalDirectory
This is basically taking all the contents inside of the cloud directory specified, and storing it inside the LocalDirectory specified.

exceptions:
	If the CloudDirectory specified does not exist, then nothing happens.
