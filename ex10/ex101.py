#!/usr/bin/env python3
import requests
import json

from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['host'] = '0.0.0.0'

bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        url = 'https://api.github.com/users/{}/repos?per_page=100&page=1'.format(username)
        response = requests.get(url)
        return render_template('index.html', ex='Ex101', repos=response.json())
    else:
        return render_template('index.html', ex='Ex101')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
