from flask import (
	flash, g, redirect, render_template,
    request, session, url_for
)

from photomanager.views.photo.bp import bp
# import Photo
# import get_database from common database module
# import current_user from flask login
# whenever deleting a photo make sure the user_id of
# the photo matches current_user.get_user().id!

# refer to view routes (photomanager/views/photo/view.py)
# for pseudo-code on how to get photos

@bp.route('/delete/confirm/<int:photo_id>')
def confirm_delete(photo_id):
	# ask the user to delete the photo
	# if they click yes delete photo
	# if not return to view of photo
	# you can use url_for('delete/perform', photo_id=photo_id)
	# to actually delete the photo

@bp.route('/delete/perform/<int:photo_id>')
def perform_delete(photo_id)
	# call Photo.delete on Photo object to perform delete