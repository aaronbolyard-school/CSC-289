from flask import (
	Blueprint, flash, g, redirect, render_template,
    request, session, url_for, abort
)

bp = Blueprint('logout', __name__, url_prefix='/logout')

@bp.route('/')
def index():
	abort(404)
