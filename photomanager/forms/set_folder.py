from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class SetFolderForm(FlaskForm):
    folder = SelectField('Folder')
    add_button = SubmitField('Add')
