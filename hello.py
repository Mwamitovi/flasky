# hello.py: A complete Flask app
import os

from flask import Flask, request, render_template, \
    session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_mail import Mail, Message

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


basedir = os.path.abspath(os.path.dirname(__file__))


# initialize the app
app = Flask(__name__)

# initialize bootstrap framework
bootstrap = Bootstrap(app)

app.config['EXPLAIN_TEMPLATE_LOADING'] = True

# secret key
app.config['SECRET_KEY'] = '7\xb2\xad\xf5\x14l\xd8tOP\xf6\n\xe9\xe1\x92q\xbf\xc6\x92_g\xec \xa5'

# application database url
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# setting false to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# setting SMTP server
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")

# initialize the database
db = SQLAlchemy(app)

# initialize migrations
migrate = Migrate(app, db)

# initialize mail
mail = Mail(app)


# static route
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        _user = User.query.filter_by(username=form.name.data).first()
        if _user is None:
            _user = User(username=form.name.data)
            db.session.add(_user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False)
    )


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


# models
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


# shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
