from app.User import bp
from flask import request, abort, jsonify, Response
from .UserService import UserService

userService = UserService()

@bp.route('/')
def base():
    return 'This is the base user route'

@bp.route('/create-user', methods=['POST'])
def createUser():
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
        
        user = userService.create_user(firstName=firstName, lastName=lastName, email=email, password=password)
        return _create_user_json(user)

@bp.route('<int:user_id>', methods=['GET'])        
def getUser(user_id):
    user = userService.get_user(user_id)
    if user:
        return _create_user_json(user)
    return Response(status=400)

@bp.route('/delete/<int:user_id>', methods=['DELETE'])
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
            "id": user.id, 
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email
        }
    )