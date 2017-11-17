import logging
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "1533763697"
