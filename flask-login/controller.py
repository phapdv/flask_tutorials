#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from compute import compute
from model import db, Users
from forms import InputForm, RegisterForm, LoginForm

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
    if user.is_authenticated is False:
        form = RegisterForm(request.form)
        if request.method == 'POST':
            userlogin = Users(form.username.data, form.password.data, form.email.data)
            try:
                db.session.add(userlogin)
                db.session.commit()
            except sqlalchemy.exc.IntegrityError:
                flash('Username or email already signed up')
                return redirect(url_for('index'))
            login_user(userlogin)
            flash('User successfully registered')
            return redirect(url_for('index'))
        return render_template('register.html', user=user)
    else:
        flash('You are already signed up')
        return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = current_user
    if user.is_authenticated is False:
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            username = form.username.data
            password = form.password.data

            registered_user = Users.query.filter_by(
                username=username, password=password).first()

            if not registered_user:
                flash('Username or Password is invalid', 'error')
                return redirect(url_for('login'))
            login_user(registered_user)
            flash('{} Logged in successfully'.format(username))
            return redirect(url_for('index'))
        return render_template('login.html', user=user)
    else:
        flash('You are already signed up')
        return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
