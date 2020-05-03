import models
from playhouse.shortcuts import model_to_dict

from flask import Blueprint ,request, jsonify

from flask_login import current_user, login_required


recipes = Blueprint('recipes','recipes')

@recipes.route('/', methods=['GET'])
@login_required
def all_recipes():
	"""show all recipes on the DB """
	current_user_recipe_dicts = [model_to_dict(recipe) for recipe in current_user.recipes]
	for recipe_dict in current_user_recipe_dicts:
		recipe_dict['creator'].pop('password')
	print(current_user_recipe_dicts)

	return jsonify({
		'data' : current_user_recipe_dicts,
		'message' : f"successfully found {len(current_user_recipe_dicts)} recipes created by logged in user ",
		'status' : 200
	}),200

@recipes.route('/add', methods=['POST'])
def add_recipe():
	""" creates a new recipe"""
	payload = request.get_json()
	new_recipe = models.Recipe.create(
		name = payload['name'],
		creator = current_user.id,
		ingredients = payload['ingredients'],
		directions = payload['directions'],
		vegan = payload['vegan'],
		gluten_free = payload['gluten_free']
	)

	recipe_dict = model_to_dict(new_recipe)

	print(recipe_dict)

	return jsonify(
			data = recipe_dict,
			message = "successfully created new recipe",
			status = 201
		), 201









