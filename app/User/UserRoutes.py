from app.user import bp
from flask import request, jsonify, Response
from .UserService import UserService
from flask_jwt_extended import jwt_required

userService = UserService()

# Secure routes
@bp.route('<int:user_id>', methods=['GET']) 
@jwt_required()
def getUser(user_id):
    user = userService.get_user_by_id(user_id)
    if user:
        return _create_user_json(user)
    return Response(status=400)

@bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def deleteUser(user_id):
    if userService.delete_user(user_id):
        return Response(status=200)
    return Response(status=400)

# Private methods    
def _create_failure_json(message):
    return jsonify({"message_key": message})

def _create_user_json(user):
    return jsonify(
        {
            "access_token": token,
            "id": user.id, 
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email
        }
    )