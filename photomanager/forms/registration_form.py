from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired()])
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators =[DataRequired()])
    
	confirm_password = PasswordField('Password', validators =[DataRequired()])
    
	registration_button = SubmitField('Register')