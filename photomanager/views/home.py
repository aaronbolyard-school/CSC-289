from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for, abort
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
@bp.route('/home')
def index():
	abort(404)
