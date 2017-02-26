from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class RepForm(FlaskForm):
	name = StringField('Name')
	location = StringField('Location')
	username = StringField('Username')
	password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])