import models

from flask import Blueprint ,request, jsonify

from flask_bcrypt import generate_password_hash, check_password_hash
# from flask.ext.bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

creators = Blueprint('creators','creators')

@creators.route('/', methods=['GET'])
def is_creator_working():
	return "creators.route at '/' GET"

@creators.route('/register', methods=['POST'])
def registration():
	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	payload['email'] = payload['email'].lower()
	print('payload',payload)

	try:
		models.Creator.get(models.Creator.email == payload['email'])

		
	except models.DoesNotExist:
		pw_hash = generate_password_hash(payload['password'])
		new_creator = models.Creator.create(
			username = payload['username'],
			email = payload['email'],
			password = payload['password']
		)

		print (new_creator)

	return "check terminal"

	