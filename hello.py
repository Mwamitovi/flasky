# hello.py: A complete Flask app
from flask import Flask, request
app = Flask(__name__)


# static route
@app.route('/')
def index():
    return '<h1>Hello,World!</h1>'


# dynamic route
@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, {}!<br/></h1><p>Your browser is {}</p>'.format(name, user_agent)
