from .UserModel import User
from app import db
from flask_jwt_extended import create_access_token, current_user

class UserService:
    def create_user(self, firstName, lastName, email, password):
        user = User(firstName=firstName, lastName=lastName, email=email)
        user.set_password(password=password)
        db.session.add(user)
        db.session.commit()
        print(User.query.all())
        return user
    
    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user and user == current_user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    def get_user_by_id(self, user_id):
        if current_user:
            return User.query.get(user_id)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()