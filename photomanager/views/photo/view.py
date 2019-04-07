from flask import (
	flash, g, redirect, render_template,
	request, session, url_for, abort
)
from flask_login import current_user, login_required

from photomanager.common.photo import tag_photo, send_photo, get_tagged_photos
from photomanager.views.photo.bp import bp
from photomanager.model.photo import Photo
from photomanager.model.user import User
from photomanager.forms.add_tag_form import AddTagForm
from photomanager.forms.query_tag_form import QueryTagForm

@bp.route('/view', methods=("GET", "POST"))
@login_required
def view():
	form = QueryTagForm()

	photos = None
	if form.validate_on_submit():
		tags = form.query.data.split(",")
		photos = []
		photo_ids = set()

		for tag in tags:
			for photo in get_tagged_photos(tag):
				if not photo[0].id in photo_ids:
					photos.append(photo[0])
					photo_ids.add(photo[0].id)
	else:
		photos = Photo.query.filter_by(user_id=current_user.get_user().id).all()
	
	return render_template("photo/view.html", photos=photos, form=form)

@bp.route('/view/<int:photo_id>', methods=("GET", "POST"))
@login_required
def single_view(photo_id):
	form = AddTagForm()
	photo = Photo.query.filter_by(id=photo_id).first()
	
	#if photo.user_id != current_user.get_user().id:
	#	abort(404)
	#else:
	if form.validate_on_submit():
			tag_photo(photo_id, form.tag.data)
			flash("Added Tag")
	return render_template("photo/view_single.html", photo=photo, form=form)

@bp.route('/get/<int:photo_id>')
@login_required
def image(photo_id):
	result = send_photo(photo_id)
	if not result:
		return abort(404)
	else:
		return result
