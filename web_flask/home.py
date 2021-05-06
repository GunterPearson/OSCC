#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, redirect, request, flash, jsonify
import os
from flask_cors import CORS
from web_flask.forms import ContactForm
from flask_mail import Message, Mail
import smtplib
app = Flask(__name__)
cors = CORS(app, resources={r"": {"origins": "*"}})
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'gunter10pearson@gmail.com'
app.config['MAIL_PASSWORD'] = 'efczcwrrpomggerp'
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_SEND'] = None
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTATCHMENTS'] = False
mail = Mail(app)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def home():
    """home route for html file"""
    form = ContactForm()
    if request.method == "POST":
        msg = Message(form.subject.data, sender=form.email.data, recipients=['oologahseniors@yahoo.com'])
        msg.body = form.name.data + "\n" + form.message.data + "\n\n" + form.email.data
        mail.send(msg)
        flash("Message is Sent!")
    return render_template("home.html")

@app.route('/events', strict_slashes=False)
def events():
    """home route for html file"""
    return render_template("events.html")

@app.route('/donate', strict_slashes=False, methods=['GET', 'POST'])
def donate():
    """home route for html file"""
    return render_template("donate.html")

@app.route('/good', strict_slashes=False, methods=['GET', 'POST'])
def good():
    """home route for html file"""
    return render_template("goodworks.html")

@app.route('/about', strict_slashes=False)
def about():
    """home route for html file"""
    return render_template("about.html")


# @app.route('/', strict_slashes=False, methods=['GET', 'POST'])
# def contact():
#     """home route for html file"""
#     return render_template("contact-us.html")

