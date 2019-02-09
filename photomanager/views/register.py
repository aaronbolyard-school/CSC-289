from photomanager.common.auth import create_user
from photomanager.forms.registration_form import RegistrationForm
from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for, abort
)

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('/', methods = ('get', 'post'))
def index():
	form = RegistrationForm()
	if form.validate_on_submit():
		if form.password.data != form.confirm_password.data:
			flash("Passwords do not match")
		elif len(form.password.data) < 8:
			flash("Password must be at least 8 characters!")
		else:
			if create_user(form.username.data, form.name.data, form.password.data):
				flash("Account successfully created!")
				return redirect(url_for("home.index"))
			else:
				flash("Account name taken!")
				
	return render_template('register.html', form=form)
