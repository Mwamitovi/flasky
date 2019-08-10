# hello.py: A complete Flask app
from flask import Flask, request, render_template, \
    session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# initialize the app
app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['SECRET_KEY'] = \
    '7\xb2\xad\xf5\x14l\xd8tOP\xf6\n\xe9\xe1\x92q\xbf\xc6\x92_g\xec \xa5'
# initialize bootstrap framework
bootstrap = Bootstrap(app)


# static route
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


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


# form
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
