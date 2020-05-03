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
	"""delete logged in creator's recipe by id"""
	try:
		recipe_to_delete = models.Recipe.get_by_id(id)

		if (recipe_to_delete.creator.id == current_user.id):
			recipe_to_delete.delete_instance()

			return jsonify(
				data={},
				message=f"DELETE SUCCESS. Deleted recipe with id of : {id}",
				status=200
			),200
		else:
			return jsonify(
				data={'error':'403 Forbidden'},
				message="User id doesnt match creator id of recipe. Creators can only delete their own added recipes"
			),403
	except models.DoesNotExist:
		return jsonify(
			data={'error':'404 Not Found'},
			messsage = "No recipes found matching that ID",
			status=404
		),404



@recipes.route('/<id>', methods=['PUT'])
@login_required
def update_recipe(id):
	"""edit and update logged in creator's recipe by id"""
	payload = request.get_json()

	recipe_to_update = models.Recipe.get_by_id(id)
	if (recipe_to_update.creator.id == current_user.id):
		recipe_to_update.name = payload['name']
		recipe_to_update.ingredients = payload['ingredients']
		recipe_to_update.directions = payload['directions']
		recipe_to_update.vegan = payload['vegan']
		recipe_to_update.gluten_free = payload['gluten_free']
		recipe_to_update.save()
		updated_recipe_dict = model_to_dict(recipe_to_update)
		updated_recipe_dict['creator'].pop('password')

		return jsonify(
			data = updated_recipe_dict,
			message = f"SUCCESS. Updated recipe with id of : {id}",
			status = 200
		),200

	else: 
		return jsonify(
			data = {'error':'403 Forbidden'},
			message = "Recipe creator's id doesnt match logged in user's id. Cannot edit another user's recipes."
		),403

@recipes.route('/<id>', methods=['GET'])
def show_recipe(id):
	recipe = models.Recipe.get_by_id(id)
	recipe_dict = model_to_dict(recipe)
	recipe_dict['creator'].pop('password')

	return jsonify(
		data = recipe_dict,
		message = f"Found recipe (id:{id})",
		status = 200
	),200































