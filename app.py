import flask
from flask import request
import json

import logging
from flask_cors import CORS

app = flask.Flask(__name__)
app.config.from_object("config.Config")
CORS(app)

logger = logging.getLogger(app.config['LOGGER_NAME'])

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/reciveNonsense')
def rcvLoad():
	print('load rcvd')
	return flask.Response(status=200)


@app.route('/reciveSense', methods=['POST', 'GET'])
def rcvThresh():

	try:

		## If the client sends a POST/GET request with nested JSON
		if flask.request.get_json():

			data = flask.request.get_json()['data']
			logger.info('The data json {0}'.format(flask.request.get_json()))

		## If the client sends a GET request with non nested values
		elif flask.request.args:

			data = flask.request.args.get('data')
			logger.info(len(flask.request.args))
			logger.info('The data args {0}'.format(flask.request.args))

		## If the client sends a POST request with non nested values
		else:

			data = flask.request.form.get('data')
			logger.info(len(flask.request.form))
			logger.info('The data form {0}'.format(flask.request.form))

		## Sanity check if data has contents
		if data:
			logger.info('data was received')
			return data
		else:
			logger.warn('data was invalid')
			return flask.Response(status=400)

	except Exception as e:

		logger.warn("Error while receiving data: {0}".format(e.args))
		return flask.Response(status=400)
		

app.run(port=8080, debug=True)
