from flask import session, redirect, url_for, render_template, request, jsonify
from . import main
from .forms import LoginForm
from ConfigParser import SafeConfigParser
import MySQLdb

parser = SafeConfigParser()
user = ""
password = ""
db = ""
host = ""

"""
try:
    parser.read("config.ini")
    print "fail here"
    user = parser.get('database', 'username')
    print "fail here 2"
    password = parser.get('database', 'password')
    print "fail here 3"
    db = parser.get('database', 'name')
    host = parser.get('database', 'host')
    
    print user, password, db, host
    
except:
    print "ERROR WITH DATABASE CALL"
"""

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login/', methods=['GET', 'POST'])
def login():
    """"Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['flightid'] = form.flightid.data
        name = checkEmailAndFlight(session['email'], session['flightid'])
        session['name'] = str(name[0])
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.email.data = session.get('email', '')
        form.flightid.data = session.get('flightid', '')
    return render_template('login.html', form=form)

def checkEmailAndFlight(email, flightId):
    database = MySQLdb.connect("turing.iamdevnull.info", "airtalk", "Thisisairtalk6364!", "airtalk")
    #database = MySQLdb.connect(host, user, password, db)
    database.query("SELECT fname FROM flightdata WHERE email='{0}' AND flight_id='{1}'".format(email, flightId))
    r = database.store_result()
    row = r.fetch_row()
    print row
    if len(row) != 0:
    	return row[0]
    return ""

@main.route('/chat/')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    email = session.get('email', '')
    name = session.get('name', '')
    flightid = session.get('flightid', '')
    if email == '' or name == "" or flightid == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=flightid)
    
