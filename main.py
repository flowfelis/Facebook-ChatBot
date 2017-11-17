import os
import logging
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def verify():
    if request.args.get('hub.challenge'):
        return request.args.get('hub.challenge')
    else:
        return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
