import os
from flask import (
	current_app, send_file
)
from flask_login import current_user

from photomanager.common.database import get_database
from photomanager.model.photo import Photo
from photomanager.model.photoTag import PhotoTag
from photomanager.model.tag import Tag

def tag_photo(photo_id, tag_name, user_id=None):
	"""
	Tags a photo.

	Returns true if the photo was tagged, false otherwise.

	If the photo already has the tag, this is considered a success.
	"""
	db = get_database()

	photo = get_photo(photo_id, user_id)
	if not photo:
		return False

	tag_name = tag_name.strip().lower()
	tag = Tag.query.filter_by(tag=tag_name).first()
	if not tag:
		tag = Tag(tag=tag_name)
		db.session.add(tag)
		db.session.commit()

	photo = get_photo(photo_id, user_id)
	photo_tag = PhotoTag(tag_id=tag.id, photo_id=photo.id)
	db.session.add(photo_tag)
	db.session.commit()

	return True

def untag_photo(photo_id, tag_name, user_id=None):
	"""
	Untags a photo.

	Returns true if the photo was untagged, false otherwise.

	If the photo already does not have the tag, this is considered a success.
	"""
	db = get_database()

	photo = get_photo(photo_id, user_id)
	if not photo:
		return False

	tag_name = tag_name.strip().lower()
	tag = Tag.query.filter_by(tag=tag_name).first()
	if not tag:
		return True

	photo_tag = PhotoTag.query.filter_by(tag_id=tag.id, photo_id=photo.id).first()

	if photo_tag:
		db.session.delete(photo_tag)

	return True

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

def get_photo_path(photo_id, user_id=None):
	"""
	Gets the path (filename) of an existing photo.

	Returns None if the photo_id does not belong to user_id.

	If user_is not provided, defaults to the currently logged
	in user.
	"""

	if user_id == None:
		user_id = current_user.get_user().id

	photo = Photo.query.filter_by(id=photo_id, user_id=user_id).first()
	if photo:
		path = os.path.join(current_app.instance_path, photo.url)
		return path

	return None

def send_photo(photo_id, user_id=None):
	"""
	Sends the full photo to the user.

	Returns None if the photo_id does not belong to user_id.

	If user_is not provided, defaults to the currently logged
	in user.
	"""

	path = get_photo_path(photo_id, user_id)
	if path:
		return send_file(path)


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

	filename = "%s/%s" % (current_app.instance_path, photo.url)
	try:
		os.remove(filename)
	except:
		# The file doesn't exist.
		pass

	db = get_database()
	db.session.delete(photo)
	db.session.commit()
