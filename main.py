import logging
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    sha = request.args.get("sha1")
    return sha
