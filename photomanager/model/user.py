from photomanager.model.main import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	name = db.Column(db.Text)

	admin = db.relationship('Admin', backref='user', cascade="all,delete")
	photos = db.relationship('Photo', backref='user', cascade="all,delete")
	folders = db.relationship('Folder', backref='user', cascade="all,delete")