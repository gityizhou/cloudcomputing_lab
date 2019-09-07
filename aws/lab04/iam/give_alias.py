# Create an alias for a CMK
import boto3
kms_client = boto3.client('kms')
alias_name = 'alias/22302319'
# CMK ID  CMK ARN
target_key_id = 'arn:aws:kms:ap-southeast-2:032418238795:key/32ecb7d2-f1cf-4f9f-bda5-563e7e15e372'
response = kms_client.create_alias(
    AliasName=alias_name,
    TargetKeyId=target_key_id
)
