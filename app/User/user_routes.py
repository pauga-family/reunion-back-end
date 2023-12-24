from app.user import bp
from flask import request, jsonify, Response
from .user_service import UserService
from flask_jwt_extended import jwt_required

user_service = UserService()

# Secure routes
@bp.route('<int:user_id>', methods=['GET']) 
@jwt_required()
def getUser(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return _user_json(user)
    return Response(status=400)

@bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def deleteUser(user_id):
    if user_service.delete_user(user_id):
        return Response(status=200)
    return Response(status=400)

@bp.route('/update/<int:user_id>', methods=["PUT"])
@jwt_required()
def updateUser(user_id):
    request_data = request.get_json()

    if request_data:
        propertiesDict = {}
        # Properties are optional
        if request_data['email'] is not None:
            propertiesDict['emal'] = request_data['email']
        if request_data['firstName'] is not None:
            propertiesDict['firstName'] = request_data['firstName']
        if request_data['lastName'] is not None:
            propertiesDict['lastName'] = request_data['lastName']
        
        # Check if we have properties to update
        if propertiesDict:
            user = user_service.update_user(user_id, propertiesDict)
            if user:
                return _user_json, 200
            else:
                return _failure_json("Unable to update user"), 422
        
        return _failure_json("No data to update"), 422
        
    return _failure_json("No data to update"), 422



# Private methods    
def _failure_json(message):
    return jsonify({"message_key": message})

def _user_json(user):
    return jsonify(
        {
            "id": user.id, 
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email
        }
    )