from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddFolderForm(FlaskForm):
    folder = StringField('Folder', validators=[DataRequired()])
    add_button = SubmitField('Add')
