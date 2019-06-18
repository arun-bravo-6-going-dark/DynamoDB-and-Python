# MoviesQuery01: Program to show how to query all movies released in a year in DynamoDB, using Python and boto3.

from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

#The region_name decides from which region the the item will be queried
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

print("Movies from 2013")

# querying all movies released in 2013
response = table.query(
    KeyConditionExpression=Key('year').eq(2013) #KeyConditionExpression to retrieve several items with the same partition key
)

for i in response['Items']:
    print(i['year'], ":", i['title'])
