from flask import session, redirect, url_for, render_template, request, jsonify
from ConfigParser import SafeConfigParser
from . import main
from .forms import LoginForm
import MySQLdb

parser = SafeConfigParser()
user = None
password = None
db = None
host = None

try:
    parser.read("/var/www/airtalk2/config.ini")
    user = parser.get('database', 'username')
    password = parser.get('database', 'password')
    db = parser.get('database', 'name')
    host = parser.get('database', 'host')

except:
    print "ERROR WITH DATABASE CALL"

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    """"Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('login.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
