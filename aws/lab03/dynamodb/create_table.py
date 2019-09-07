import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='cloudfiles1',
    KeySchema=[
        {
            'AttributeName': 'userid',
            'KeyType': 'HASH'
        }

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'userid',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='cloudfiles1')

# Print out some data about the table.
print(table.item_count)