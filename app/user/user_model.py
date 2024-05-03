from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum

class UserRole(Enum):
    STANDARD = 'standard'
    COMMITTEE = 'committee'
    ADMIN = 'admin'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True, unique=False)
    lastName = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64), index=False, unique=False)

    """role = db.Column(db.Enum(UserRole), default=UserRole.STANDARD) 
    would line 18 be better? 'Since you've already defined an Enum for 
    user roles (UserRole), it would be better to use that enum directly 
    in your model'"""

    def __repr__(self):
        return '<User {}>'.format(self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

