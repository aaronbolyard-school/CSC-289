from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QueryTagForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    search_button = SubmitField('Search')
