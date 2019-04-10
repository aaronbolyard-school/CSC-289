from photomanager.model.main import db

class Admin(db.Model):
	id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,)
	vision_api_key = db.Column(db.Text)
