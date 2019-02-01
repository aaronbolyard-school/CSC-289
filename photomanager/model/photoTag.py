from photomanager.model.main import db

class PhotoTag(db.Model):
	tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
	photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'), primary_key=True)
