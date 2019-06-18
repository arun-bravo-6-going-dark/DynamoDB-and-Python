# MoviesDeleteTable: Program to show how to delete a table in DynamoDB, using Python and boto3.
from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.

#The region_name decides in which region the table will be deleted
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

table.delete()
