import os
import logging
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
    data = request.get_json() # cannot return this
    app.logger.debug(data)

    return data


if __name__ == '__main__':
    app.run(debug=True)
