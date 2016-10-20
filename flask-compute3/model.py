#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from wtforms import Form, FloatField, validators


class InputForm(Form):
    """docstring for InputForm."""
    r = FloatField('Input R', validators=[validators.InputRequired()])
