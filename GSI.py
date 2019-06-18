import boto3

# Boto3 is the AWS SDK library for Python.
# You can use the low-level client to make API calls to DynamoDB.
client = boto3.client('dynamodb', region_name='us-east-1')

try:
    resp = client.update_table(
        TableName='Movies',
        # Any attributes used in your new global secondary index must be declared in AttributeDefinitions
        AttributeDefinitions=[
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
        ],
        # This is where you add, update, or delete any global secondary indexes on your table.
        GlobalSecondaryIndexUpdates=[
            {
                'Create': {
                    # You need to name your index and specifically refer to it when using it for queries.
                    'IndexName': 'title-Index',
                    # Like the table itself, you need to specify the key schema for an index.
                    # For a global secondary index, you can use a simple or composite key schema.
                    'KeySchema': [
                        {
                            'AttributeName': 'title',
                            'KeyType': 'HASH'
                        }
                    ],
                    # You can choose to copy only specific attributes from the original item into the index.
                    # You might want to copy only a few attributes to save space.
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    # Global secondary indexes have read and write capacity separate from the underlying table.
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1,
                    }
                }
            }
        ],
    )
    print("Secondary index added!")
except Exception as e:
    print("Error updating table:")
    print(e)