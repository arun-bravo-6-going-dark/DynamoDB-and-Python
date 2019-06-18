# MoviesCreateTableLSI: Program to show how to create a table with Local Secondary Index in DynamoDB, using Python and boto3.

from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.

dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 

table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[                 #key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        },
    ],
    LocalSecondaryIndexes=[    #Represents the properties of a local secondary index.
        {
            'IndexName': 'LSIMovies',
            'KeySchema': [
                {
                    'AttributeName': 'year',
                    'KeyType': 'HASH'    
                },
                {
                    'AttributeName': 'rating',
                    'KeyType': 'RANGE'
                }
            ],
            # Note: since we are projecting all the attributes of the table
                # into the LSI, we could have set ProjectionType=ALL and
                # skipped specifying the NonKeyAttributes
            'Projection': {
                'ProjectionType': 'INCLUDE',
                'NonKeyAttributes': ['rating', 'running_time_secs']
            }
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'rating',
            'AttributeType': 'N'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }        
)

print("Table status:", table.table_status)
