from flask_login import (
	LoginManager, login_user, logout_user, current_user,
	login_required
)
from werkzeug.security import generate_password_hash, check_password_hash

from photomanager.common.database import get_database
from photomanager.model.user import User

login_manager = LoginManager()

class LoggedInUser:
	def __init__(self, user):
		self._user = user
		if user:
			self.is_authenticated = True
			self.is_active = True
			self.is_anonymous = False

	def get_user(self):
		return self._user

	def get_id(self):
		if self._user:
			return str(self._user.id)
		else:
			return "0"

def init_app(app):
	login_manager.init_app(app)
	login_manager.login_view = "home.index"

	@login_manager.user_loader
	def load_user(user_id):
		user = User.query.filter_by(id=int(user_id)).first()
		return LoggedInUser(user)

def create_user(email, name, password):
	user = User.query.filter_by(email=email).first()
	if user:
		return False

	password = generate_password_hash(password)

	db = get_database()
	user = User(email=email, name=name, password=password)
	db.session.add(user)
	db.session.flush()
	return True
	
def login(email, password):
	user = User.query.filter_by(email=email).first()
	if not user:
		return False

	if not check_password_hash(user.password, password):
		return False

	login_user(LoggedInUser(user))
	return True

def logout():
	logout_user()
