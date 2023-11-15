from flask_jwt_extended import create_access_token, current_user, get_jwt, get_jwt_identity
from app.user.UserModel import User
from app.user.UserService import UserService
from app import jwt
from datetime import datetime, timedelta, timezone

class AuthService:
    userService =  UserService()

    def log_user_in(self, email, password):
        user = self.userService.get_user_by_email(email)
        if user:
            print(user)
            if user.check_password(password):
                token = self._create_jwt_token(user)
                return token
            return None
        return None
    
    def _create_jwt_token(self, user):
        access_token = create_access_token(identity=user)
        return access_token

    # Register a callback function that takes whatever object is passed in as the
    # identity when creating JWTs and converts it to a JSON serializable format.
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id


    # Register a callback function that loads a user from your database whenever
    # a protected route is accessed. This should return any python object on a
    # successful lookup, or None if the lookup failed for any reason (for example
    # if the user has been deleted from the database).
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()