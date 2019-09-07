import boto3

ec2 = boto3.client('ec2')
response1 = ec2.describe_key_pairs()
for keys in response1["KeyPairs"]:
    print(keys["KeyName"])

# print(response)


response2 = ec2.create_key_pair(KeyName='yizhou-key')
print(response2)
