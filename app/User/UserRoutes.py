import json
from flask import Response, app, request, abort
from app.User import UserService, bp

@bp.route('/')
def base():
    return 'This is the base user route'

@bp.route('/create-user', methods=['POST'])
def create_user():
	
	request_data = request.get_json()
	response = Response(mimetype='application/json')

	if request_data:
		try:
			email = request_data['email']
			firstName = request_data['firstName']
			lastName = request_data['lastName']
			password = request_data['password']
		
			if not isinstance(email, str) or not isinstance(firstName, str) or not isinstance(lastName, str) or not isinstance(password, str):
				response.status = 400
				response.response = create_failure_json("Invalid data")

				abort(response)
		except:
			response.status = 442
			response.response = create_failure_json("Missing data")
			abort(response)
		return UserService.create_user(firstName=firstName, lastName=lastName, email=email, password=password)
	
def create_failure_json(message):
	return json.dumps({"messag_key": message})


@bp.errorhandler(400)
def handle_bad_request(error):
    return 'Bad Request: Wrong data type found in the form.', 400

@bp.errorhandler(422)
def handle_unprocessable_entity(error):
    return 'Bad Request: No information found in the form.', 400