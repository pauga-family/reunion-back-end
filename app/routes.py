from flask import request
from app import app

@app.route('/')
def inded():
	return "Hello, World!"

@app.route('/create-user', methods=['POST'])
def create_user():
	
	request_data = request.get_json()
	
	if request_data:
		
		if 'emailAddress' in request_data:
			if isinstance(request_data['emailAddress'],str):
				emailAddress = request_data['emailAddress']
		if 'firstName' in request_data:
			if isinstance(request_data['firstName'],str):
				firstName = request_data['firstName']
		if 'lastName' in request_data:
			if isinstance(request_data['lastName'],str):
				lastName = request_data['lastName']
		if 'password' in request_data:
			if isinstance(request_data['password'],str):
				password = request_data['password']
	
	return '''
			Email Address = {}
			First Name = {}
			Last Name = {}
			Password = {}
	'''.format(emailAddress,firstName,lastName,password)