from flask import Flask,jsonify
from resources.creators import creators
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True #while we are in development , dont use in a production deployment
PORT=8000

app=Flask(__name__)

app.secret_key = "ScoobyDoobyDooWhereAreYou"
login_manager = LoginManager()
login_manager.init_app(app)

CORS(creators, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(creators, url_prefix='/api/v1/creators')


@app.route('/')
def hello():
	return 'Hello, world!'

# @login_manager.creator_loader














if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
