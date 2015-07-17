#!/usr/bin/env  python
#coding:utf-8

from flask import Flask
from app1.demo import app1
from app2.login import app2

app = Flask(__name__)
app.debug = True
app.register_blueprint(app1)
app.register_blueprint(app2)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=11111)