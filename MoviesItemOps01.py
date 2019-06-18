# MoviesItemsOps01: Program to show how to create a new item in a table in DynamoDB, using Python and boto3.
from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

#The region_name decides in which region the item will be created
dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 

table = dynamodb.Table('Movies')

title = "The Big New Movie"
year = 2015

#putting an item into the 'Movies' table
response = table.put_item(
   Item={
        'year': year,
        'title': title,
        'info': {
            'plot':"Nothing happens at all.",
            'rating': decimal.Decimal(0)
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
