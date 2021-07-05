import pytest

import messages
from datetime import datetime

'''
Simple test module. 

Testing functions to send and receive messages from/to AWS-SQS

francisco@garciac.es
'''

def test_send_message():
    date = datetime.today()
    outtest = messages.send_message("{} -- Hi, this is a test".format(date))
    if outtest and isinstance(outtest, str):
        assert True
    else:
        assert False

def test_receive_message():
    message = messages.receive_message()
    print("---\n{}\n---".format(message['Body']))

    if message == "":
        assert False
    else:
        assert True
