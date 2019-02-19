import os
from flask import (
	current_app
)
from flask_login import current_user

from photomanager.common.database import get_database
from photomanager.model.photo import Photo

def get_photo(photo_id, user_id=None):
	"""
	Gets an existing photo.

	Returns None if the photo_id does not belong to user_id.

	If user_is not provided, defaults to the currently logged
	in user.
	"""

	if user_id == None:
		user_id = current_user.get_user().id

	return Photo.query.filter_by(id=photo_id, user_id=user_id).first()

def create_photo(name, user_id=None):
	"""
	Create a photo without any file data with the given name.

	The photo is assigned to the currently logged in user
	if user_id is not specified.
	"""

	if user_id == None:
		user_id = current_user.get_user().id

	db = get_database()
	photo = Photo(name=name, user_id=user_id)
	db.session.add(photo)
	db.session.flush()

	return photo

def upload_new_photo(name, file, user_id=None):
	"""
	Creates a new photo and uploads it.

	The photo is assigned to 'user_id' if provided. Otherwise,
	the currently logged in user is assigned the photo.

	Returns the newly created photo.
	"""
	# Create photo entry
	photo = create_photo(name)

	# Save photo
	upload_existing_photo(photo, file)

	return photo

def upload_existing_photo(photo, file):
	"""
	Overwrites an existing photo.
	"""
	_, extension = os.path.splitext(file.filename)
	local_filename = "photos/%d%s" % (photo.id, extension)
	filename = "%s/%s" % (current_app.instance_path, local_filename)

	try:
		root_path = "%s/photos" % current_app.instance_path
		if not os.path.exists(root_path):
			os.makedirs(root_path)
	except:
		# os.path.exists -> os.makedirs is not atomic.
		# The directory can be created between those calls.
		# So we really don't care if the directory exists.
		pass

	file.save(filename)

	# Update photo
	photo.url = local_filename

	db = get_database()
	db.session.add(photo)
	db.session.commit()

def rename_photo(photo, name):
	"""
	Renames a photo.
	"""
	photo.name = name

	db = get_database()
	db.session.add(photo)
	db.session.commit()

def delete_photo(photo):
	"""
	Deletes a photo.

	The photo is removed from storage as well.
	"""

	filename = "%s/%s" % (current_app.instance_path, local_filename)
	try:
		os.remove(filename)
	except:
		# The file doesn't exist.
		pass

	db = get_database()
	db.session.delete()
	db.session.commit()
