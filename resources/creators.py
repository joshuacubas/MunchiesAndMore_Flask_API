import models

from flask import Blueprint ,request, jsonify

from flask_bcrypt import generate_password_hash, check_password_hash



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
		return jsonify(
			data = {},
			message = f"User with {payload['email']} email address already exists.",
			status = 401		
		),401
		
	except models.DoesNotExist:
		pw_hash = generate_password_hash(payload['password'])
		new_creator = models.Creator.create(
			username = payload['username'],
			email = payload['email'],
			password = pw_hash
		) 

		print ("new creator:",new_creator)

		login_user(new_creator)

		new_creator_dict = model_to_dict(new_creator)

		print ("new_creator_dict",new_creator_dict)

		print(type(new_creator_dict['password']))

		new_creator_dict.pop('password')

		return jsonify(
		data = new_creator_dict,
		message = f"SUCCESS, new creator has been registered as {new_creator_dict['email']}",
		status = 201
		),201

@creators.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	print("payload",payload)
	# print("payload[username]",payload['username'])
	# print("payload[pw]",payload['password'])

	# return "check terminal"



	try:
		creator = models.Creator.get(models.Creator.email == payload['email'])
		creator_dict =model_to_dict(creator)
		password_works = check_password_hash(creator_dict['password'],payload['password'])
		if (password_works):
			login_user(creator)
			creator_dict.pop('password')

			return jsonify(
				data = creator_dict,
				message = f"Successfully logged in as {creator_dict['email']}",
				status = 200
			), 200
		else:
			print("Password is Incorrect")
			return jsonify(
				data = {},
				message = "Email/password is incoreect",
				status = 404
			),401
	
	except models.DoesNotExist:
		print('username is no good, does not exist')
		return jsonify(
			data = {},
			message = "Incorrect email/password",
			status=401
		),401


@creators.route('/logout', methods=["GET"])
def logout():
	logout_user()
	print("logout route")
	return jsonify(
		data={},
		message="successfully logged out",
		status=200
	),200

@creators.route('/logged_in', methods=['GET'])
def logged_in():
	if current_user : 
		print(current_user) 
	if not current_user.is_authenticated:
		return jsonify(
			data={},
			message="No user is logged in",
			status=401
		),401
	else:
		creator_dict = model_to_dict(current_user)
		creator_dict.pop('password')
		return jsonify(
			data = creator_dict,
			message = f"Currently logged in with {creator_dict['email']} email address.",
			status = 200
		),200

	return '/logged_in route reached, check terminal'































	