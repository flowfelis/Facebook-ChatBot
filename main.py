import os
import json
import requests
import traceback
from flask import Flask, request, redirect
from watson_developer_cloud import ToneAnalyzerV3

# tone_analyzer = ToneAnalyzerV3(
#     username = os.environ.get('TONE_USERNAME'),
#     password = os.environ.get('TONE_PASSWORD'),
#     version = os.environ.get('TONE_VERSION'))

tone_analyzer = ToneAnalyzerV3(
    username = 'bf4d9c4a-a8d3-4599-97b5-63ea77b665d6',
    password = 'oe8mEef2JXQv',
    version = '2017-09-26')

# page_token = os.environ.get('PAGE_ACCESS_TOKEN')
# verify_token = os.environ.get('VERIFY_TOKEN')
page_token = 'EAAKW1Cjtl8IBALKCaKVaQXUpEQ1Bb8Ki7bSVEOl0T7DCKpfdgRdmOC3BUfKmxxxN8zAL0HVZB3zGhhLWGYGnwreOnSTmGFbN6ewCDSsXZB91JI1PQAxjUfPsAcQ9CEpwXZA3UMizQ5Hz9ZAXqQ7ePyEoMxgewrnaWGKrnVoFxQZDZD'
verify_token = 'myToken'
app = Flask(__name__)


@app.route('/')
def index():
    if verify_token is not None and request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    else:
        return "<h1>Welcome to ChatBot App.</h1> <h4>Please go to Facebook and find " \
        "Mr. Chat Bot for a fun chit-chat :)</h4><quote>Developed By Flowfelis</quote>"

@app.route('/', methods=['POST'])
def receive():
    data = request.get_json()
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    receive_text = data['entry'][0]['messaging'][0]['message']['text']

    tone_data = tone_analyzer.tone(tone_input=receive_text, sentences=False,
        content_type="text/plain")

    # print(json.dumps(tone_analyzer.tone(tone_input=receive_text, tones='emotion',
        # sentences=False, content_type="text/plain"), indent=2))

    # collect emotions
    emotions = ['anger', 'fear', 'joy', 'sadness']
    tones = tone_data['document_tone']['tones']
    import pdb; pdb.set_trace()

    # for emo in tones:


    send_text = "Hi There!"

    payload = {'recipient': {'id': sender_id}, 'message': {'text': send_text}}

    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + page_token, json=payload)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)
