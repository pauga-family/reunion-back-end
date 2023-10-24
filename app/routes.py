from flask import request
from app import app

@app.route('/')
def inded():
	return "Hello, World!"

# "methods = post" will allow for only POST requests
@app.route('/create-user', methods=['POST'])
def create_user():
	emailAddress = None
	firstName = None
	lastName = None
	password = None
	# processes JSON data and converts to variables
	request_data = request.get_json()
	# check if variables exist in JSON request
	if request_data:
		#isinstance(data,dataType) returns True if data is of type dataType, False if else
		#each if case checks if the data is in JSON request, and then checks if it is correct data type
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
	#returns information sent from user
	return '''
			Email Address = {}
			First Name = {}
			Last Name = {}
			Password = {}
	'''.format(emailAddress,firstName,lastName,password)