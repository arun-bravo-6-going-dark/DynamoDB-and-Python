# MoviesQuery02: Program to show how to query all movies released in a year with certain titles in DynamoDB, using Python and boto3.

from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

#The region_name decides from which region the the item will be queried
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

print("Movies from 2013 - titles A-L, with genres and lead actor")

# Query all movies released in a year with certain titles
response = table.query(
    ProjectionExpression="#yr, title, info.genres, info.actors[0]", #A projection expression is a string that identifies the attributes you want
    ExpressionAttributeNames={ "#yr": "year" }, # Expression Attribute Names for Projection Expression only.
    KeyConditionExpression=Key('year').eq(2013) & Key('title').between('A', 'L')
)

for i in response[u'Items']:
    print(json.dumps(i, cls=DecimalEncoder))
