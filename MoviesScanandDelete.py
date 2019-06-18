# MoviesScanandDelete: A sample program to show how to delete all the items in a table in DynamoDB, using Python and boto3.

from __future__ import print_function # Python 2/3 compatibility
from botocore.exceptions import ClientError
import boto3 # Boto3 is the AWS SDK library for Python.
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

pe = "#yr, title"
# Expression Attribute Names for Projection Expression only.
ean = { "#yr": "year", }
esk = None


response = table.scan(
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )

# Deleting all the items
try:
    for i in response['Items']:

        delRecord = table.delete_item(
            Key={
                'year': i["year"],
                'title': i["title"]
            }
        )
        print("delete completed")
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise