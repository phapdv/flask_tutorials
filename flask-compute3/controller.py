#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash
from compute import compute

from model import InputForm

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'sljdfkasdfakl;;fa'


@app.route('/hw3', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST':
        if form.validate():
            r = form.r.data
            s = compute(r)
        else:
            s = None
            flash('Please input R')
    else:
        s = None
    return render_template('view.html', form=form, s=s)

if __name__ == '__main__':
    app.run(debug=True)
