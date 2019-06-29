# hello.py: A complete Flask app
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, Martin!</h1>'
