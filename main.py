import os
import json
import requests
import traceback
import logging
from flask import Flask, request, redirect, session
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
app.secret_key = 'my_unique_secret_key'

class Bot():
    """Bot class"""
    def __init__(self, result):
        try:
            self.result = result[0]
        except Exception as e:
            self.result = None
        self.answers = {
            'positive': 'Oh, that\'s very kind of you',
            'neutral': 'Interesting. Ok.',
            'negative': 'I feel so bad about what you wrote',
            }
        self.positiveEmotions = ['joy']
        self.negativeEmotions = ['anger', 'fear', 'sadness']
        # self.mood = 0


    def reply(self):
        """This is returning the final answer"""
        if self.result in self.negativeEmotions:
            return self.answers['negative']
        elif self.result in self.positiveEmotions:
            return self.answers['positive']
        else:
            return self.answers['neutral']

    def evalMood(self):
        """Evaluate Mood (positive, negative, neutral)"""
        session['mood'] = 0
        if self.result in self.negativeEmotions:
            session['mood'] -= 1
        if self.result in self.positiveEmotions:
            session['mood'] += 1



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

    # collect emotions from tones
    emotions = ['anger', 'fear', 'sadness', 'joy']
    tones = tone_data['document_tone']['tones']

    # use list comprehension
    # [ expression for item in list if conditional ]
    result = [i['tone_id'] for i in tones if i['tone_id'] in emotions]
    bot = Bot(result)
    bot.evalMood()
    print(session['mood'])

    send_text = bot.reply()

    payload = {'recipient': {'id': sender_id}, 'message': {'text': send_text}}

    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + page_token, json=payload)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)
