from app.User import bp
from flask import request, abort
from .UserService import UserService

userService = UserService()

@bp.route('/')
def base():
    return 'This is the base user route'

@bp.route('/create-user', methods=['POST'])
def createUser():
    request_data = request.get_json()
    
    if request_data:
        # if 'email' in request_data:
        #     if isinstance(request_data['email'],str):
        #         email = request_data['email']
        if 'email' in request_data:
            email = request_data['email']
        if 'firstName' in request_data:
            firstName = request_data['firstName']
        if 'lastName' in request_data:
            lastName = request_data['lastName']
        if 'password' in request_data:
            password = request_data['password']

        if email is None or firstName is None or lastName is None or password is None:
            abort(422, description='Missing data')

        if not isinstance(email, str) or not isinstance(firstName, str) or not isinstance(lastName, str) or not isinstance(password, str):
            abort(400, description='Incorrect format')

        # return '''email is {},
        # firstName is {},
        # lastName is {}
        # password is {}'''.format(email, firstName, lastName, password)
        return userService.create_user(firstName=firstName, lastName=lastName, email=email, password=password)