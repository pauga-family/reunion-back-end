from .UserModel import User
from app import db
from werkzeug.security import generate_password_hash

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
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    def get_user(self, user_id):
        return User.query.get(user_id)
