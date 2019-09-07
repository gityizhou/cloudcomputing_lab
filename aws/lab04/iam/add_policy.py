import boto3
import json
s3 = boto3.client('s3')
bucket_name = '22302319-cloudcomputing'
bucket_policy={
  "Version": "2012-10-17",
  "Statement": {
   "Sid": "AllowAllS3ActionsInUserFolderForUserOnly",
    "Effect": "DENY",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::22302319-cloudcomputing",
    "Condition": {
      "StringNotLike": {
          "aws:username":"22302319@student.uwa.edu.au"
       }
    }
  }
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)
# Set the new policy
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
