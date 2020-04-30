from flask import Flask

DEBUG=True #while we are in development , dont use in a production deployment
PORT=8000

app=Flask(__name__)
if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)

