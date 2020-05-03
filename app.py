from flask import Flask,jsonify
from resources.creators import creators
from resources.recipes import recipes
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True #while we are in development , dont use in a production deployment
PORT=8000

app=Flask(__name__)

app.secret_key = "ScoobyDoobyDooWhereAreYou"
login_manager = LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_creator(user_id):
	try:
		print("loading the following creator")
		user= models.Creator.get_by_id(user_id)
		return user
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={
			'error':'User is not logged in',
		},
		message= "Must be logged in to have access granted",
		status=401
	),401



CORS(creators, origins=['http://localhost:3000'], supports_credentials=True)

CORS(recipes, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(creators, url_prefix='/api/v1/creators')

app.register_blueprint(recipes, url_prefix='/api/v1/recipes')











if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
