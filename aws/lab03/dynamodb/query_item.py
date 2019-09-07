import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('cloudfiles1')
response = table.get_item(
    Key={
        'userid': '1001',
    }
)
item = response['Item']
print(item)
