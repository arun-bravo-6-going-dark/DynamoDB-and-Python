# MoviesCreateTable: Program to show how to create a table in DynamoDB, using Python and boto3.
from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.


#The region_name decides in which region the table will be created
dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 

#Creating the table named 'Movies'
table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[                #key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },                     #usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }                       #stores items with the same partition key physically close together, in sorted order by the sort key value
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N' #the attribute is of type Number
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S' #the attribute is of type String
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10, #The maximum number of strongly consistent reads consumed per second before DynamoDB
        'WriteCapacityUnits': 10 #The maximum number of writes consumed per second before DynamoDB
    }
)

print("Table status:", table.table_status)