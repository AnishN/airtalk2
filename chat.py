#!/bin/env python
from gevent import monkey
monkey.patch_all()
from app import create_app, socketio

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import jsonify

app = create_app(True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")
    
@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == '__main__':
    socketio.run(app)
