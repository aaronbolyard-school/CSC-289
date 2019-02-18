from flask import (
	flash, g, redirect, render_template,
    request, session, url_for
)

from photomanager.views.photo.bp import bp

@bp.route('/upload')
def upload(photo_id):
	# upload photo
	# send photo to Google to get tags
	# etc
