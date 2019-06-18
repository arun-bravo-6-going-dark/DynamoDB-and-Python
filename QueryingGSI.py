import time

import boto3 
from boto3.dynamodb.conditions import Key

# Boto3 is the AWS SDK library for Python.
# The "resources" interface allows for a higher-level abstraction than the low-level client interface.
# For more details, go to http://boto3.readthedocs.io/en/latest/guide/resources.html
#The region_name decides from which region the the item will be queried
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Movies')

# When adding a global secondary index to an existing table, you cannot query the index until it has been backfilled.
# This portion of the script waits until the index is in the “ACTIVE” status, indicating it is ready to be queried.
while True:
    if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
        print('Waiting for index to backfill...')
        time.sleep(5)
        table.reload()
    else:
        break

# When making a Query call, you use the KeyConditionExpression parameter to specify the hash key on which you want to query.
# If you want to use a specific index, you also need to pass the IndexName in our API call.
resp = table.query(
    # Add the name of the index you want to use in your query.
    IndexName="title-Index",
    KeyConditionExpression=Key('title').eq('Rush'),
)

print("The query returned the following items:")
for item in resp['Items']:
    print(item)