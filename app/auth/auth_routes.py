from app.auth import bp
from ..user.user_service import UserService
from flask import request, jsonify
from .auth_service import AuthService
from flask_jwt_extended import jwt_required

user_service = UserService()
auth_service = AuthService()

@bp.route('/create-user', methods=['POST'])
def create_user():
    request_data = request.get_json()
    
    if request_data:
        try:
            email = request_data['email']
            firstName = request_data['firstName']
            lastName = request_data['lastName']
            password = request_data['password']

            if not isinstance(email, str) or not isinstance(firstName, str) or not isinstance(lastName, str) or not isinstance(password, str):
                return _create_failure_json("Invalid data"), 400

        except:
            return _create_failure_json("Missing data"), 422
        
        user = user_service.create_user(firstName=firstName, lastName=lastName, email=email, password=password)
        user, token = auth_service.log_user_in(email=email, password=password)
        if token is None:
            return _create_failure_json("Something went wrong"), 400
        return _create_user_json(user, token)
    
@bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()

    if request_data:
        try:
            email = request_data['email']
            password = request_data['password']

            if not isinstance(email, str) or not isinstance(password, str):
                return _create_failure_json("Invalid data"), 400
            
        except:
            return _create_failure_json("Missing data"), 422
        
        user, token = auth_service.log_user_in(email, password)

        if user:
            return _create_user_json(user, token)
        return _create_failure_json("Invalid email or password"), 400
    return _create_failure_json("No data"), 400


# Private methods    
def _create_failure_json(message):
    return jsonify({"message_key": message})

def _create_user_json(user, token):
    return jsonify(
        {
            "access_token": token,
            "id": user.id, 
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email
        }
    )