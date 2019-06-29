# first flasky app
from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, Wordl!</h1>'
