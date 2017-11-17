import os
import logging
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    if request.args.get('hub.challenge'):
        return request.args.get('hub.challenge')
    else:
        return "<h1>Welcome to ChatBot App.</h1> <h4>Please go to Facebook and find " \
        "Mr. Chat Bot for a fun chit-chat :)</h4>"

@app.route('/', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode())
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}}
            return "<p>text: {0}</p><p>sender: {1}</p>".format(text, sender)
            # r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            print(traceback.format_exc())
    elif request.method == 'GET':

if __name__ == '__main__':
    app.run(debug=True)
