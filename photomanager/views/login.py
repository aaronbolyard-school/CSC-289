
from photomanager.common.auth import login
from photomanager.forms.login_form import LoginForm
from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['GET','POST'])
def index():
        form = LoginForm()
        if form.validate_on_submit():
                if login(form.username.data, form.password.data):
                        flash("Successfully Logged in!")
                        return redirect(url_for("home.index"))
                else:
                        flash("Username or password is invalid.")
        return render_template("login.html", form=form)
