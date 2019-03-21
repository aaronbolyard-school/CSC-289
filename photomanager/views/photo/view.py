from flask import (
	flash, g, redirect, render_template,
    request, session, url_for, abort
)
from flask_login import current_user, login_required

from photomanager.common.photo import send_photo
from photomanager.views.photo.bp import bp
from photomanager.model.photo import Photo
from photomanager.model.user import User

@bp.route('/view')
@login_required
def view():
	photos = Photo.query.filter_by(user_id=current_user.get_user().id).all()
	
	return render_template("photo/view.html", photos=photos)

@bp.route('/view/<int:photo_id>')
@login_required
def single_view(photo_id):
	photo = Photo.query.filter_by(id=photo_id).first()
	
	if photo.user_id != current_user.get_user().id:
		return abort(404)
	else:
		return render_template("photo/view_single.html", photo=photo)

@bp.route('/get/<int:photo_id>')
@login_required
def image(photo_id):
	result = send_photo(photo_id)
	if not result:
		return abort(404)
	else:
		return result
