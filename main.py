import os
import json
import requests
from flask import Flask, request, redirect
from watson_developer_cloud import ToneAnalyzerV3
from bot import Bot


tone_analyzer = ToneAnalyzerV3(
    username = os.environ.get('TONE_USERNAME'),
    password = os.environ.get('TONE_PASSWORD'),
    version = os.environ.get('TONE_VERSION'))

page_token = os.environ.get('PAGE_ACCESS_TOKEN')
verify_token = os.environ.get('VERIFY_TOKEN')


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
    global moodLevel
    data = request.get_json()
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    receive_text = data['entry'][0]['messaging'][0]['message']['text']

    tone_data = tone_analyzer.tone(tone_input=receive_text, sentences=False,
    content_type="text/plain")
    emotions = ['anger', 'fear', 'sadness', 'joy']
    tones = tone_data['document_tone']['tones']
    result = [i['tone_id'] for i in tones if i['tone_id'] in emotions]
    bot = Bot(result)

    if receive_text == 'mood':
        moodText = bot.getMood()
        print(moodText)
        send_text = moodText + ' / Mood Level: {}'.format(bot.readFile())
    else:
        bot.evalMood()
        print("Mood Level: {}".format(bot.readFile()))
        send_text = bot.reply()

    payload = {'recipient': {'id': sender_id}, 'message': {'text': send_text}}
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + page_token, json=payload)
    return 'Message Sent'


if __name__ == '__main__':
    app.run(debug=True)
