import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

print "creating ProductCatalog table ......."

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='ProductCatalog',
    KeySchema=[
        {
            'AttributeName': 'Id',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Id',
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
);

print "ProductCatalogue table created!"

print "creating Forum table ......."

table = dynamodb.create_table(
    TableName='Forum',
    KeySchema=[
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 5
    }
);


print "Forum table created!"

print "creating Thread table ......."

table = dynamodb.create_table(
    TableName='Thread',
    KeySchema=[
        {
            'AttributeName': 'ForumName',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Subject',
            'KeyType': 'RANGE'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ForumName',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Subject',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 5
    }
);

print "Thread table created!"

print "creating Reply table ......."

table = dynamodb.create_table(
    TableName='Reply',
    KeySchema=[
        {
            'AttributeName': 'ForumName',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Subject',
            'KeyType': 'RANGE'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'ReplyDateTime',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'PostedBy',
            'AttributeType': 'S'
        },

    ],

    LocalSecondaryIndexes=[
        {
        'IndexName': 'PostedBy-index',

            'KeySchema': [
                {
                    'AttributeName': 'Id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'PostedBy',
                    'KeyType': 'RANGE'
                },
            ],
        'Projection' : [
                'ProjectionType': 'KEYS_ONLY',
                ],
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'ReplyDateTime',
            'KeyType': 'RANGE'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 5
    }
);

print "Reply table created"
