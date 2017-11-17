import os
import requests
from flask import Flask, request

page_token = os.environ.get('PAGE_ACCESS_TOKEN')
verify_token = os.environ.get('VERIFY_TOKEN')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == verify_token:
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
        # return "<h1>Welcome to ChatBot App.</h1> <h4>Please go to Facebook and find " \
        #     "Mr. Chat Bot for a fun chit-chat :)</h4><hr><quote>Developed By Flowfelis</quote>"
    if request.method == 'POST':
        data = request.get_json()
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        receive_text = data['entry'][0]['messaging'][0]['message']['text']
        send_text = "Hi There!"
        payload = {'recipient': {'id': sender_id}, 'message': {'text': send_text}}

        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + page_token, json=payload)
        pass

if __name__ == '__main__':
    app.run(debug=True)
