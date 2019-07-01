# hello.py: A complete Flask app
from flask import Flask, request, render_template
app = Flask(__name__)


# static route
@app.route('/')
def index():
    return render_template('index.html')


# dynamic route
@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return render_template('user.html', name=name, user_agent=user_agent)
