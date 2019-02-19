from flask import (
	flash, g, redirect, render_template,
    request, session, url_for
)
from flask_login import login_required

from photomanager.views.photo.bp import bp
from photomanager.forms.photo_upload_form import PhotoUploadForm
from photomanager.common.photo import (
	get_photo, upload_new_photo, upload_existing_photo, rename_photo
)

@bp.route('/upload', methods=('GET', 'POST'))
@bp.route('/upload/<int:photo_id>', methods=('GET', 'POST'))
@login_required
def upload(photo_id=None):
	form = PhotoUploadForm()
	if photo_id != None and request.method == 'GET':
		photo = get_photo(photo_id)

		if not photo:
			flash("Photo not found.")
			return redirect("home.index")

		form.name.data = photo.name

	if form.validate_on_submit():
		photo = None
		if photo_id != None:
			photo = get_photo(photo_id)
			if not photo:
				flash("Photo not found.")
				return redirect("home.index")

			if form.image.data != None:
				upload_existing_photo(photo, form.image.data)

			rename_photo(photo, form.name.data)
		else:
			if form.image.data == None:
				flash("Please upload a photo.")
			else:
				photo = upload_new_photo(form.name.data, form.image.data)

		if photo != None:
			flash("Photo saved!")
			return redirect(url_for("photos.upload", photo_id=photo.id))

	return render_template("photo/upload.html", form=form)
