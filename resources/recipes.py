import models
from playhouse.shortcuts import model_to_dict

from flask import Blueprint ,request, jsonify

from flask_login import current_user, login_required


recipes = Blueprint('recipes','recipes')

@recipes.route('/', methods=['GET'])
def is_recipe_working():
	return "recipe.route at '/' GET"