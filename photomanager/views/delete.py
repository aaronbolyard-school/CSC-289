# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:40:55 2019

@author: n_zwa
"""
from flask import (
        Blueprint, flash, g, direct, render_template,
        request, session, url_for
        )

bp = Blueprint('home', __name__, url_prefix= '/')


from photomanager.common.database import get_database
from photomanager.model.user import user

@bp.route('/')
@bp.route('/')
def index():
    users = User.query.filter_by(email="zwann@faytechcc.edu").all()
    
    db = get_database()
    db.session.delete(photo)
    db.session.commit()
    
    return render_template('Submission.html', users=users)

    if Query_delete.lower() == Yes:
        db = get_database()
        db.session.delete('<int:photo_id>')
        commit()
        
        # if not return to view of photo
    else:
        @bp.route('/view/<int:photo_id>')
        
        

	# you can use url_for('delete/perform', photo_id=photo_id)

	# to actually delete the photo


	# call Photo.delete on Photo object to perform delete

@bp.route('/delete/perform/<int:photo_id>')
def perform_delete(photo_id):
    
    url__for(delete, '<int:photo_id>')


