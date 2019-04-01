from flask_login import current_user

from photomanager.common.database import get_database
from photomanager.model.photo import Photo
from photomanager.model.folder import Folder
from photomanager.model.folderPhoto import FolderPhoto

def add_photo_to_folder(photo, folder, user_id=None):
	if photo.user_id != folder.user_id:
		return False

	if user_id == None:
		user_id = current_user.get_user().id

	if photo.user_id != user_id:
		return False

	folderPhoto = FolderPhoto(user_id=user.id, folder_id=folder.id)

	db = get_database()
	db.session.add(folderPhoto)
	db.session.commit()

	return True

def get_photos(folder, user_id=None):
	if user_id == None:
		user_id = current_user.get_user().id

	if folder.user_id != user_id:
		return None

	folderPhotos = FolderPhoto.query.filter_by(folder_id=folder.id)

	result = []
	for i in folderPhotos:
		result.append(Photo.query.filter_by(id=i.photo_id).first())

	return result

def remove_photo_from_folder(photo, folder):
	if photo.user_id != folder.user_id:
		return False

	folderPhoto = FolderPhoto(user_id=user.id, folder_id=folder.id)
	
	db = get_database()
	db.session.delete(folderPhoto)
	db.session.commit()

	return True

def delete_folder(folder, user_id=None):
	if user_id == None:
		user_id = current_user.get_user().id

	if folder.user_id != user_id:
		return False

	db = get_database()
	photos = FolderPhoto.query.filter_by(foler_id=folder.id).all()
	for photo in photos:
		db.session.delete(photo)
	db.session.delete(folder)
	db.session.commit()

	return True

def add_folder(name, user_id=None):
	if user_id == None:
		user_id = current_user.get_user().id

	name = name.strip()

	folder = Folder(name=name, user_id=user_id)
	db = get_database()
	db.session.add(folder)
	db.session.commit()

	return folder
