from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTagForm(FlaskForm):
    tag = StringField('Tag', validators=[DataRequired()])
    add_button = SubmitField('Add')
