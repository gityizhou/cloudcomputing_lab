import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
# print(response)

'''
Put this code into a python file
tabulate the print to have 2 columns with Endpoint and RegionName
'''

for region in response['Regions']:
    print(f"{region['Endpoint']}: {region['RegionName']}")


'''
pip3 install awscli
pip3 install boto3

aws configure
AWS Access Key ID [None]: <access key id>
AWS Secret Access Key [None]: <secret access key>
Default region name [None]: ap-southeast-2
Default output format [None]: json

aws ec2 describe-regions --output table
'''