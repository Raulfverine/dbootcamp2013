"""
Test post data. Make sure 
"""
import requests
import urllib
import json
import email
import hashlib
from test_data import test_data1, test_data2, test_data3

def process_email_header(data):
    response = {}
    msg = email.message_from_string(data)
    for each in msg.keys():
        if each not in response:
            response[each] = msg[each]
    return response

data = {'clipboard_data':test_data3}
#sha1 = hashlib.sha1(test_data3).hexdigest()
#print "Send data sha1: ", sha1

r = requests.post("http://ec2-54-254-97-253.ap-southeast-1.compute.amazonaws.com:8000/post", data=data)

if r.json() == process_email_header(test_data3):
	print "Test case success"
else:
	print "Test case failed"