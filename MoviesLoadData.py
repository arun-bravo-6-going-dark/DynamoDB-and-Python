# MoviesLoadData: Program to show how to Load items into a table in DynamoDB, using Python and boto3.

from __future__ import print_function # Python 2/3 compatibility
import boto3 # Boto3 is the AWS SDK library for Python.
import json
import decimal

#The region_name decides in which region the items will be uploaded
dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 

table = dynamodb.Table('Movies')

# Uploading file movie1.json
with open("movie1.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )