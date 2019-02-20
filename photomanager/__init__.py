import os

from flask import Flask

from flask_bootstrap import Bootstrap

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	app.config.from_pyfile("settings.cfg")
	
	Bootstrap(app)

	from photomanager.common.database import init_app as init_database
	init_database(app)
	from photomanager.common.auth import init_app as init_auth
	init_auth(app)
	import photomanager.views.login
	app.register_blueprint(photomanager.views.login.bp)
	import photomanager.views.home
	app.register_blueprint(photomanager.views.home.bp)
	import photomanager.views.register
	app.register_blueprint(photomanager.views.register.bp)
	import photomanager.views.photo.main
	import photomanager.views.photo.bp
	app.register_blueprint(photomanager.views.photo.bp.bp)

	return app
