from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for, abort
)

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('/')
def index():
	abort(404)
