import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from photomanager.model.main import db

import photomanager.model.admin
import photomanager.model.folder
import photomanager.model.folderPhoto
import photomanager.model.photo
import photomanager.model.photoTag
import photomanager.model.tag
import photomanager.model.user

def get_database():
	"""
	Gets the database.

	If the database is not open, connects to the database.
	Expects the database to be stored at the "database" key.

	Returns the database.
	"""
	if 'database' not in g:
		g.database = db

	return g.database

def flush_database():
	db = get_database()
	db.session.commit()

def close_database(app):
	"""
	Closes the databases, freeing all resources.
	"""
	pass

def initialize_database():
	"""
	Initializes the database from the model.
	"""
	database = get_database()
	database.create_all()

def init_app(app):
	db.init_app(app)

	app.teardown_appcontext(close_database)
	app.cli.add_command(initialize_database_command)
	app.cli.add_command(add_admin_command)

@click.command('initialize-database')
@with_appcontext
def initialize_database_command():
	"""
	Clear the existing data and create new tables.
	"""
	initialize_database()
	click.echo('Initialized the database.')

@click.command('add-admin')
@click.option('--email')
@click.option('--password')
@click.option('--name')
@with_appcontext
def add_admin_command(email, password, name):
	"""
	Adds an admin account with the provided credentials.
	"""

	password = generate_password_hash(password)

	db = get_database()
	user = photomanager.model.user.User(email=email, name=name, password=password)
	db.session.add(user)
	db.session.flush()
	admin = photomanager.model.admin.Admin(id=user.id)
	db.session.add(admin)
	db.session.commit()

	click.echo("Added admin: " + name)
