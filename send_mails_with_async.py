# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail, Message
from threading import Thread

from keys import *


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = 'Mail from Flask: \t'
app.config['FLASKY_MAIL_SENDER'] = 'This is a Flask test <flasky@example.com>'
app.config['FLASKY_ADMIN'] = the_reciper

mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, message):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + '' + subject,
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = "Hello"
    msg.html = message
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

reciper = raw_input('Para quien es el mail? \n')
subject = raw_input('Cual será el asunto? \n')
message  = raw_input('Que le quieres enviar? \n')


send_email(reciper, subject, message)
