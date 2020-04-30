import models

from flask import Blueprint ,request, jsonify
# from flask_bcrypt import generate_password_hash, check_password_has
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

creators = Blueprint('creators','creators')

@creators.route('/', methods=['GET'])
def is_creator_working():
	return "creators.route at ,/, GET"