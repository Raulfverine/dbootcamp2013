import email
import urllib
import hashlib
from test_data import test_data1
from flask import Flask, jsonify, request, make_response, current_app
from datetime import timedelta
from functools import update_wrapper
import base64

app = Flask(__name__)
import json

def test_response():
    response = {}
    msg = email.message_from_string(test_data1)
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

def crossdomain(origin=None, methods=None, headers=None,
            max_age=21600, attach_to_all=True,
            automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/test")
def index():
    return jsonify(test_response())


@app.route('/post', methods = ['POST', 'GET'])
@crossdomain(origin='*', headers='Content-Type')
def getDataFromClient():
    clipboard_data  = str(request.form['clipboard_data']) #Instant fix. Without str() it is unicode.
    print clipboard_data
    clipboard_data = base64.b64decode(clipboard_data)
    #print hashlib.sha1(clipboard_data).hexdigest()
    print clipboard_data
    result = process_email_header(clipboard_data)
    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True, host="ec2-54-254-97-253.ap-southeast-1.compute.amazonaws.com", port=8000)
