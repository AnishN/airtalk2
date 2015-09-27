#!/usr/bin/python

import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/airtalk2/python-eggs' 

activate_this = '/var/www/airtalk2/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/airtalk2')
sys.path.append('/var/www/airtalk2')

from hello import app as application
