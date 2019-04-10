from photomanager.model.main import db

class Photo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	url = db.Column(db.Text)
	name = db.Column(db.Text)

	tags = db.relationship('PhotoTag', backref='photo', cascade="all,delete")
