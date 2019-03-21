from flask import (
        Blueprint, flash, g, redirect, render_template,
        request, session, url_for
)
from flask_login import (
    current_user, login_required
)

from photomanager.common.photo import delete_photo
from photomanager.model.photo import Photo
from photomanager.views.photo.bp import bp

@bp.route('/delete/confirm/<int:photo_id>')
@login_required
def confirm_delete(photo_id):
    photo = Photo.query.filter_by(id=photo_id).first()
    if photo.user_id != current_user.get_user().id:
        return abort(404)
    else:
        return render_template("photo/confirm_delete.html", photo=photo)

@bp.route('/delete/perform/<int:photo_id>')
@login_required
def perform_delete(photo_id):
    photo = Photo.query.filter_by(id=photo_id).first()
    if photo.user_id != current_user.get_user().id:
        return abort(404)
    else:
        delete_photo(photo)
        return redirect(url_for("photos.view"))
