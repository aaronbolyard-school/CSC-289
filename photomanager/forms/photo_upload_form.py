from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PhotoUploadForm(FlaskForm):
	image = FileField('Image')
	name = StringField('Name', validators=[DataRequired()])
	save = SubmitField("Save")