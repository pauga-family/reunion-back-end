from flask import app, request, abort
from app.User import bp

@bp.route('/')
def base():
    return 'This is the base user route'

@app.route('/create-user', methods=['POST'])
def create_user():
	
	request_data = request.get_json()
	try :
		if request_data:
			if 'emailAddress' not in request_data:
				abort(422)
			if 'firstName' not in request_data:
				abort(422)
			if 'lastName' not in request_data:
				abort(422)
			if 'password' not in request_data:
				abort(422)
			if not isinstance(request_data['emailAddress'],str):
				abort(400)
			if not isinstance(request_data['firstName'],str):
				abort(400)
			if not isinstance(request_data['lastName'],str):
				abort(400)
			if not isinstance(request_data['password'],str):
				abort(400)
			
			emailAddress = request_data['emailAddress']
			firstName = request_data['firstName']
			lastName = request_data['lastName']
			password = request_data['password']
		
		return '''
				Email Address = {}
				First Name = {}
				Last Name = {}
				Password = {}
		'''.format(emailAddress,firstName,lastName,password)
	

	except:
		return '''
			There was an exception.
		'''

@app.errorhandler(400)
def handle_bad_request(error):
    return 'Bad Request: Wrong data type found in the form.', 400

@app.errorhandler(422)
def handle_unprocessable_entity(error):
    return 'Bad Request: No information found in the form.', 400