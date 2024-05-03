from .user_model import User, UserRole
from app import db
from flask_jwt_extended import current_user
from typing import Dict

class UserService:
    def create_user(self, firstName, lastName, email, password):
        user = User(firstName=firstName, lastName=lastName, email=email)
        user.set_password(password=password)
        user.role = UserRole.STANDARD.value #do I need .value here?
        db.session.add(user)
        db.session.commit()

        return user
    
    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user and user == current_user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    def update_user(self, user_id, updatedProperties: Dict[str, str]):
        user = User.query.get(user_id)
        if user is None or user != current_user:
            return None
        
        if isinstance(updatedProperties, Dict):
            for key, value in updatedProperties.items():
                if key == "firstName":
                    user.firstName = value
                if key == "lastName":
                    user.lastName = value
                if key == "email":
                    user.email = value
            db.session.commit()    
            
            return user

    
    def get_user_by_id(self, user_id):
        if current_user:
            return User.query.get(user_id)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()