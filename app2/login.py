#!/usr/bin/env  python
#coding:utf-8

from flask import render_template, flash, redirect,Blueprint
from forms import LoginForm

# index view function suppressed for brevity
app2 = Blueprint('app2', __name__)


@app2.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)

