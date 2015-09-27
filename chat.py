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

if __name__ == '__main__':
    socketio.run(app)
