import json,time,sys
from collections import OrderedDict
import boto3
from boto3.dynamodb.conditions import Key,Attr
import myaws

# Set table name
DYNAMO_TABLE_NAME = "youtubeComments"

def get_items(start_time):
    dynamo = myaws.getResource('dynamodb')
    table = dynamo.Table(DYNAMO_TABLE_NAME)
    items = table.scan(FilterExpression=Attr('timestamp').between(start_time, start_time+4))['Items']
    toxic_count = 0
    for item in items: 
        toxic_count += int(item['label'])
    clean_count = len(items) - toxic_count
    return clean_count, toxic_count
