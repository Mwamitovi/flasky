# hello.py: A complete Flask app
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

# initialize the app
app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
# initialize bootstrap framework
bootstrap = Bootstrap(app)


# static route
@app.route('/')
def index():
    return render_template('index.html')


# dynamic route
@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return render_template('user.html', name=name, user_agent=user_agent)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
