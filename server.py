'''
AWS-SQS Demo

Simple Web Service frontend to send and receive messages from AWS SQS service.
This web service runs on port 5000.

francisco@garciac.es
'''
import flask
from flask import request, jsonify

import messages as msg

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Testing site</h1><p>AWS SQS demo</p>"

@app.route('/api/v1/messages', methods=['GET'])
def api_get_messages():
    messages = msg.receive_message()
    print (messages)
    return jsonify(messages)

@app.route('/api/v1/send', methods=['POST'])
def api_create_mensaje():
    json = request.get_json(force=True)

    if json.get('message') is None:
        return jsonify({'message': 'Bad request'}), 400

    mensaje = json['message']
    res = msg.send_message(mensaje)
    
    return jsonify({'res': mensaje })


app.run()
