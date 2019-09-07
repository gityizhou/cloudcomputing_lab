import os
import boto3
import base64

# ------------------------------
# CITS5503
#
# cloudstorage.py
#
# skeleton application to copy local files to S3
#
# Given a root local directory, will return files in each level and
# copy to same path on S3
#
# ------------------------------ 


ROOT_DIR = '.'
# user name
ROOT_S3_DIR = '22302319-cloudcomputing'

s3 = boto3.resource("s3")

bucket_config = {'LocationConstraint': 'ap-southeast-2'}


def upload_file(folder_name, file, file_name):
    # upload
    s3.meta.client.upload_file(file.replace("./", ""), ROOT_S3_DIR,
                               "{}/{}".format(folder_name.rstrip("/"), file_name).replace("./", ""))
    print("Uploading %s" % file)


# Main program
# Insert code to create bucket if not there
s3 = boto3.client('s3')
bucket = s3.create_bucket(Bucket=ROOT_S3_DIR,
                          CreateBucketConfiguration=bucket_config)

if bucket.creation_date:
    print("The bucket exists")
else:
    print(f"The bucket does not exist, a new bucket {ROOT_S3_DIR} created")

# try:
#
#     print(response)
# except Exception as error:
#     pass


# parse directory and upload files

for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
    if dir_name != ROOT_DIR:
        for fname in file_list:
            upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)

print("done")
