import email
import urllib

from flask import Flask, jsonify, request
app = Flask(__name__)
import json

def test_response():
    response = {}
    msg = email.message_from_string(zharif)
    for each in msg.keys():
        if each not in response:
            response[each] = msg[each]
    return response

def process_email_header(email_data):
    response = {}
    print type(email_data)
    print email_data
    msg = email.message_from_string(email_data)
    for each in msg.keys():
        if each not in response:
            response[each] = msg[each]
    print response
    return response

@app.route("/test")
def index():
    return jsonify(test_response())


@app.route('/post', methods = ['POST'])
def getDataFromClient():
    print "getDataFromClient"
    clipboard_data  = str(request.form['clipboard_data'])
    print clipboard_data
    import hashlib
    print hashlib.sha1(clipboard_data).hexdigest()
    result = process_email_header(clipboard_data)
    print "RESULT"
    print type(result)
    print result
    print "------"
    
    return jsonify(result)
    

    
if __name__ == "__main__":
    app.run(debug=True, host="ec2-54-254-97-253.ap-southeast-1.compute.amazonaws.com", port=8000)
