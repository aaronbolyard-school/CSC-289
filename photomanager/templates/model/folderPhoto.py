from photomanager.model.main import db

class FolderPhoto(db.Model):
	folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'), primary_key=True)
	photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'), primary_key=True)
