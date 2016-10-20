#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from compute import compute
from model import db, Users
from forms import InputForm, RegisterForm, LoginForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from app import app

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)


@app.route('/hw3', methods=['GET', 'POST'])
def index():
    user = current_user
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
    return render_template('view.html', form=form, s=s, user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    user = current_user
    form = RegisterForm(request.form)
    if request.method == 'POST':
        user = Users(form.username.data, form.password.data, form.email.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('User successfully registered')
        return redirect(url_for('index'))
    return render_template('register.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = current_user
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        registered_user = Users.query.filter_by(username=username, password=password).first()
        if registered_user is None:
            flash('Username or Password is invalid', 'error')
        login_user(registered_user)
        flash('Logged in successfully')
        return redirect(url_for('index'))
    return render_template('login.html', user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
