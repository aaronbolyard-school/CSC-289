from flask import (
	flash, g, redirect, render_template,
	request, session, url_for, abort
)
from flask_login import current_user, login_required

from photomanager.common.photo import tag_photo, send_photo, get_tagged_photos
from photomanager.views.photo.bp import bp
from photomanager.model.photo import Photo
from photomanager.model.folderPhoto import FolderPhoto
from photomanager.model.folder import Folder
from photomanager.model.user import User
from photomanager.forms.add_tag_form import AddTagForm
from photomanager.forms.set_folder_form import SetFolderForm
from photomanager.forms.query_tag_form import QueryTagForm
from photomanager.common.folder import get_folders, add_photo_to_folder, get_photos

@bp.route('/view', methods=("GET", "POST"))
@bp.route('/view/<int:folder_id>', methods=("GET", "POST"))
@login_required
def view(folder_id=None):
	form = QueryTagForm()
	folder = None
	if folder_id:
		folder = Folder.query.filter_by(id=folder_id).first()
		if folder.user_id != current_user.get_user().id:
			return abort(404)

	photos = None
	folders = get_folders()
	if form.validate_on_submit():
		tags = form.query.data.split(",")
		photos = []
		photo_ids = set()

		for tag in tags:
			for photo in get_tagged_photos(tag):
				if not photo[0].id in photo_ids:
					if not folder or FolderPhoto.query.filter_by(folder_id=folder_id, photo_id=photo[0].id).first():
						photos.append(photo[0])
						photo_ids.add(photo[0].id)
	else:
		if folder:
			photos = get_photos(folder)
		else:
			photos = Photo.query.filter_by(user_id=current_user.get_user().id).all()
	
	return render_template("photo/view.html", photos=photos, form=form, folders=folders, folder=folder)

@bp.route('/single/<int:photo_id>', methods=("GET", "POST"))
@login_required
def single_view(photo_id):
	tagForm = AddTagForm(prefix="tag")
	folderForm = SetFolderForm(prefix="folder")
	photo = Photo.query.filter_by(id=photo_id).first()
	
	folders = get_folders()
	folderForm.folder.choices = [(str(f.id), f.name) for f in folders]

	if photo.user_id != current_user.get_user().id:
		abort(404)
	else:
		if tagForm.add_button.data and tagForm.validate_on_submit():
			tag_photo(photo_id, tagForm.tag.data)
			flash("Added Tag")
		if folderForm.add_button.data and folderForm.validate_on_submit():
			folder = Folder.query.filter_by(id=int(folderForm.folder.data)).first()
			add_photo_to_folder(photo, folder)
			flash("Added Folder")

	return render_template("photo/view_single.html", photo=photo, tagForm=tagForm, folderForm=folderForm, folders=folders)

@bp.route('/get/<int:photo_id>')
@login_required
def image(photo_id):
	result = send_photo(photo_id)
	if not result:
		return abort(404)
	else:
		return result
