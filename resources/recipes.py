import models
from playhouse.shortcuts import model_to_dict

from flask import Blueprint ,request, jsonify

from flask_login import current_user, login_required


recipes = Blueprint('recipes','recipes')


@recipes.route('/', methods=['GET'])
def all_recipes():
	"""show all recipes on the DB """
	all_recipe_dicts = [model_to_dict(recipe) for recipe in models.Recipe.select()]
	# for recipe_dict in current_user_recipe_dicts:
	# 	recipe_dict['creator'].pop('password')
	print(all_recipe_dicts)

	return jsonify({
		'data' : all_recipe_dicts,
		'message' : f"successfully found {len(all_recipe_dicts)} recipes created by all the users ",
		'status' : 200
	}),200




@recipes.route('/myrecipes', methods=['GET'])
@login_required
def all_recipes_from_logged_in_user():
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
@login_required
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

@recipes.route('/<id>', methods=['DELETE'])
@login_required
def delete_recipe(id):
	delete_query = models.Recipe.delete().where(models.Recipe.id == id)
	num_of_rows_deleted=delete_query.execute()
	print(num_of_rows_deleted)
	return jsonify(
		data={},
		message=f"Successfully deleted {num_of_rows_deleted} recipes, with id {id}",
		status = 200,
	),200

@recipes.route('/<id>', methods=['PUT'])
@login_required
def update_recipe(id):
	payload=request.get_json()

	update_query = models.Recipe.update(
		name = payload['name'],
		creator = current_user.id,
		ingredients = payload['ingredients'],
		directions = payload['directions'],
		vegan = payload['vegan'],
		gluten_free = payload['gluten_free']
	).where(models.Recipe.id == id)

	num_of_rows_changed = update_query.execute()

	updated_recipe = models.Recipe.get_by_id(id)

	updated_recipe_dict = model_to_dict(updated_recipe)

	return jsonify(
		data={},
		message=f"Successfully update recipe with id of {id}",
		status=200
	),200



























