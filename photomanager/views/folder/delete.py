from flask import (
        Blueprint, flash, g, redirect, render_template,
        request, session, url_for
)
from flask_login import (
    current_user, login_required
)

from photomanager.common.folder import delete_folder
from photomanager.views.folder.bp import bp
from photomanager.model.folder import Folder

@bp.route('/delete/confirm/<int:folder_id>')
@login_required
def confirm_delete(folder_id):
	folder = Folder.query.filter_by(id=folder_id).first()
	
	if folder.user_id != current_user.get_user().id:
		return abort(404)
	else:
		return render_template("folder/confirm_delete.html", folder=folder)

@bp.route('/delete/perform/<int:folder_id>')
@login_required
def perform_delete(folder_id):
	folder = Folder.query.filter_by(id=folder_id).first()
	
	if folder.user_id != current_user.get_user().id:
		return abort(404)
	else:
		delete_folder(folder)
		return redirect(url_for("photos.view"))
