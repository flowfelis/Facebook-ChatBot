import logging
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    sha = request.args.get("sha1")
    return sha

if __name__ == '__main__':
    app.run(debug=True)
