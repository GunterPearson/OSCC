#!/usr/bin/python3
"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class ContactForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField('Name', validators=[DataRequired()])

    subject = StringField(
        'Subject',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
