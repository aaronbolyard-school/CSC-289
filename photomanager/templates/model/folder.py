from photomanager.model.main import db

class Folder(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	name = db.Column(db.Text)
	public = db.Column(db.Boolean)

	photos = db.relationship('FolderPhoto', backref='folder', cascade="all,delete")
