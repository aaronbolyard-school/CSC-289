from photomanager.model.main import db

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tag = db.Column(db.Text, nullable=False, unique=True)

	tags = db.relationship('PhotoTag', backref='tag', cascade="all,delete")
