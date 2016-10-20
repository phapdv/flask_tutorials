#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import wtforms as wtf
from model import db, Users


class InputForm(wtf.Form):
    """docstring for InputForm."""
    r = wtf.FloatField('Input R', validators=[wtf.validators.InputRequired()])


class RegisterForm(wtf.Form):
    username = wtf.StringField('Username', validators=[wtf.validators.InputRequired()])
    password = wtf.PasswordField('Password', validators=[wtf.validators.Required()])
    confirm_password = wtf.PasswordField('Confirm Password', validators=[
        wtf.validators.Required(),
        wtf.validators.EqualTo('confirm_password', message='Password must match')])
    email = wtf.StringField('email', validators=[wtf.validators.InputRequired()])


class LoginForm(wtf.Form):
    username = wtf.StringField('Username', validators=[wtf.validators.InputRequired()])
    password = wtf.PasswordField('Password', validators=[wtf.validators.Required()])
