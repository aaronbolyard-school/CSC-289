from flask import (
	flash, g, redirect, render_template,
    request, session, url_for, abort
)

from photomanager.views.photo.bp import bp
# import Photo
from photomanager.model.photo import Photo
# import current_user from flask login
from photomanager.model.user import User

@bp.route('/view')
def view():
	pass
	# use current_user.get_user().id with
	# use Photo.query.filter_by to find all 
	# photos of the user
	photos = Photo.query.filter_by(user_id=current_user.get_user().id).all()
	
	# render template "view" with photos
	return render_template("view.html", photos=photos)

@bp.route('/view/<int:photo_id>')
def single_view(photo_id):
	pass
	# use Photo.query.filter_by to find a photo with
	# photo_id
	photo = photo.query.filter_by(id=photo_id).first()
	
	# make sure the current_user matches the user_id
	# of the fetched photo
	# if not return abort(404)
	if photo.user_id != current_user.get_user().id:
	 	return abort(404)
	else:
	# otherwise return render template "view_single" with photo
		return render_template("view.html", photo_id=photo_id)
	