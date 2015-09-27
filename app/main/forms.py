from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    email = StringField('Email', validators=[Required()])
    flightid = StringField('Flight #', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
