from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for, abort
)

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/')
def index():
	abort(404)
