from flask import (
	flash, g, redirect, render_template,
    request, session, url_for
)
from flask_login import login_required

from photomanager.views.folder.bp import bp

from photomanager.common.folder import add_folder

from photomanager.forms.add_folder_form import AddFolderForm

@bp.route("/add", methods=("GET", "POST"))
@login_required
def add():
	form = AddFolderForm()
	if form.validate_on_submit():
		if add_folder(form.folder.data):
			flash("Added Folder")

			return redirect(url_for("photos.view"))
		else:
			flash("Failed to add folder. Folder may already exist.")

	return render_template("folder/add.html", form=form)
