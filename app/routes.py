import string
from flask import request
from app import app

@app.route('/')
def inded():
	return "Hello, World!"

# "methods = post" will allow for only POST requests
@app.route('/create-user', methods=['POST'])
def create_user():
	# processes JSON data and converts to variables
	request_data = request.get_json()
	#initializing variables
	emailAddress = None
	firstName = None
	lastName = None
	password = None
	# check if variables exist in JSON request
	if request_data:
		if 'emailAddress' in request_data:
			emailAddress = request_data['emailAddress']
		if 'firstName' in request_data:
			firstName = request_data['firstName']
		if 'lastName' in request_data:
			lastName = request_data['lastName']
		if 'password' in request_data:
			password = request_data['password']
	#returns information sent from user
	return '''
			Email Address = {}
			First Name = {}
			Last Name = {}
			Password = {}
	'''.format(emailAddress,firstName,lastName,password)

#someone commented saying another useful 
#method is "request.form.to_dict()" which takes
#information from the form and 
#automatically returns it in dictionary form
