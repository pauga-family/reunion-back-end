from .UserModel import User
from app import db
from werkzeug.security import generate_password_hash

class UserService:
    def create_user(self, firstName, lastName, email, password):
        user = User(firstName=firstName, lastName=lastName, email=email)
        user.set_password(password=password)
        return 'User info: First Name: {}, Last Name: {}, email: {}, password hash: {}'.format(user.firstName, user.lastName, user.email, user.password_hash)
    
    # def login(self, user):
