from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

class SetFolderForm(FlaskForm):
    folder = SelectField('Folder', validators=[DataRequired()])
    add_button = SubmitField('Add')
