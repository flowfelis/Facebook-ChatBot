import os
import requests
import traceback
from flask import Flask, request, redirect

page_token = os.environ.get('PAGE_ACCESS_TOKEN')
verify_token = os.environ.get('VERIFY_TOKEN')
app = Flask(__name__)


@app.route('/')
def index():
    return "hello world!"
if __name__ == '__main__':
    app.run(debug=True)
