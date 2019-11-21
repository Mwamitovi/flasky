from threading import Thread
from flask_mail import Message
from flask import current_app, render_template
from . import mail


def send_async_email(_app, msg):
    with _app.app_context():
        mail.send(msg)


# email support
# noinspection PyProtectedMember
def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + " " + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
