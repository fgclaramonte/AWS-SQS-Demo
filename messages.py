'''
AWS SQS. 


'''
import boto3
import os

os.environ['AWS_PROFILE'] = "profile1"

sqs = boto3.client('sqs', region_name='us-east-2')

queue_url = 'https://sqs.us-east-2.amazonaws.com/338433442274/cola1'


def send_message(mensaje):
    # Send message to the queue
    response = sqs.send_message(
        QueueUrl=queue_url, 
        DelaySeconds=10,
        MessageAttributes={
        },
        MessageBody=(
            format(mensaje)
        )
    )

    if response:
        print(response['MessageId'])
        return response['MessageId']

    else:
        return False


def receive_message():
    try:
        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SendTimeStamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        message = response['Messages'][0]
        print("---\n{}\n---".format(message['Body']))

        '''
        # Optional code for remove messages.
        receipt_handle = message['ReceiptHandle']
        # Delete received message from queue
        sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
        )
        '''
        print('received and deleted message: %s' % message)
    except:
        message ="No pending messages"
    return message
