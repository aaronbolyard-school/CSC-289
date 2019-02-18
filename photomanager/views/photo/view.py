from flask import (
	flash, g, redirect, render_template,
    request, session, url_for
)

from photomanager.views.photo.bp import bp
# import Photo
# import current_user from flask login

@bp.route('/view')
def view():
	# use current_user.get_user().id with
	# use Photo.query.filter_by to find all 
	# photos of the user
	#
	# render template "view" with photos

@bp.route('/view/<int:photo_id>')
def single_view(photo_id)
	# use Photo.query.filter_by to find a photo with
	# photo_id
	#
	# make sure the current_user matches the user_id
	# of the fetched photo
	#
	# if not return abort(404)
	#
	# otherwise return render template "view_single" with photo
