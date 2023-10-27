from app.User import bp
from flask import request, abort, Response, json
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
                response = Response(response=json.dumps({"message_key": "Incorrect format"}),
                                status=400,
                                mimetype='application/json')
                abort(response)

        except KeyError:
            response = Response(response=json.dumps({"message_key": "Missing data"}),
                                status=422,
                                mimetype='application/json')
            abort(response)
        
        return userService.create_user(firstName=firstName, lastName=lastName, email=email, password=password)