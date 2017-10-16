

import boto3
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')

# Wait until the table exists.
#table.meta.client.get_waiter('table_exists').wait(TableName='ProductCalalog')

# Print out some data about the table.
table = dynamodb.Table('ProductCatalog')
print("ProductCatalog table contains " table.item_count "records")
print
print......
print
print("...Now adding data to ProductCatalog table ...")

with table.batch_writer() as batch:
    batch.put_item(
    Item={
         'Id': '1101',
        'Title': 'Book 101 Title',
        'ISBN': '111-1111111111',
        'Authors': 'Author1',
        'Price': '2',
        'Dimensions': '8.5 x 11.0 x 0.5',
        'PageCount': '500',
        'InPublication': '1',
        'ProductCategory': 'Book',
        }
    )

    batch.put_item(
    Item={
        'Id': '102',
        'Title': 'Book 102 Title',
        'ISBN': '222-2222222222',
        'Authors': ['Author1', 'Author2'],
        'Price': '20',
        'Dimensions': '8.5 x 11.0 x 0.8',
        'PageCount': '600',
        'InPublication': '1',
        'ProductCategory': 'Book'
        }
    )

    batch.put_item(
    Item={
        'Id': '103',
        'Title': 'Book 103 Title',
        'ISBN': '333-3333333333',
        'Authors': ['Author1', 'Author2'],
        'Price': '2000',
        'Dimensions': '8.5 x 11.0 x 1.5',
        'PageCount': '600',
        'InPublication': '0',
        'ProductCategory': 'Book'
        }
    )

    batch.put_item(
    Item={
        'Id': '201',
        'Title': '18-Bike-201',
        'Description': '201 Description',
        'BicycleType': 'Road',
        'Brand': 'Mountain A',
        'Price': '100',
        'Gender': 'M',
        'Color': ['Red', 'Black'],
        'ProductCategory': 'Bicycle'
        }
    )

    batch.put_item(
    Item={
        'Id': '202',
        'Title': '21-Bike-202',
        'Description': '202 Description',
        'BicycleType': 'Road',
        'Brand': 'Brand-Company A',
        'Price': '200',
        'Gender': 'M',
        'Color': ['Green', 'Black'],
        'ProductCategory': 'Bicycle'
        }
    )

    batch.put_item(
    Item={
        'Id': '203',
        'Title': '19-Bike-203',
        'Description': '203 Description',
        'BicycleType': 'Road',
        'Brand': 'Brand-Company B',
        'Price'; '300',
        'Gender': 'W',
        'Color': ['Red', 'Green', 'Black'],
        'ProductCategory': 'Bicycle'
        }
    )

    batch.put_item(
    Item={
        'Id': '204',
        'Title': '18-Bike-204',
        'Description': '204 Description',
        'BicycleType': 'Mountain',
        'Brand': 'Brand-Company B',
        'Price': '400',
        'Gender': 'W',
        'Color': ['Red'],
        'ProductCategory': 'Bicycle'
        }
    )

    batch.put_item(
    Item={
        'Id': '205',
        'Title': '20-Bike-205',
        'Description': '205 Description',
        'BicycleType': 'Hybrid',
        'Brand': 'Brand-Company C',
        'Price': '500',
        'Gender': 'B',
        'Color': ['Red', 'Black'],
        'ProductCategory': 'Bicycle'
        }
    )


# Print out some data about the table.
table = dynamodb.Table('Forum')
print("Forum table contains " table.item_count "records")
print
print......
print
print("...Now adding data to Forum table ...")

with table.batch_writer() as batch:
    batch.put_item(
    Item={
        'Name': 'Amazon DynamoDB',
        'Category': 'Amazon Web Services'),
        'Threads': '0',
        'Messages': '0',
        'Views': '1000'
        }
    )

    batch.put_item(
    Item={
        'Name': 'Amazon S3',
        'Category': 'Amazon Web Services',
        'Threads': '0'
        }
    )



# Print out some data about the table.

table = dynamodb.Table('Reply')
print("Reply table contains " table.item_count "records")
print
print......
print
print("...Now adding data to Reply table ...")

date_now = datetime.now()

with table.batch_writer() as batch:
    batch.put_item(
    Item={
        'Id': 'Amazon DynamoDB#DynamoDB Thread 1',
        'ReplyDateTime': date_now - timedelta(days=14),
        'Message': 'DynamoDB Thread 1 Reply 2 text',
        'PostedBy': 'User B'
        }
    )

    batch.put_item(
    Item={
        'Id': 'Amazon DynamoDB#DynamoDB Thread 2',
        'ReplyDateTime': date_now - timedelta(days=21),
        'Message': 'DynamoDB Thread 2 Reply 3 text',
        'PostedBy': 'User B'
        }
    )

    batch.put_item(
    Item={
        'Id': 'Amazon DynamoDB#DynamoDB Thread 2',
        'ReplyDateTime': date_now - timedelta(days=7),
        'Message': 'DynamoDB Thread 2 Reply 2 text',
        'PostedBy': 'User A'
        }
    )

    batch.put_item(
    Item={
        'Id': 'Amazon DynamoDB#DynamoDB Thread 2',
        'ReplyDateTime': date_now - timedelta(days=1),
        'Message': 'DynamoDB Thread 2 Reply 1 text',
        'PostedBy': 'User A'
        }
    )
print "done......"
