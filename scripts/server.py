#!/usr/bin/env python3
from flask import Flask, jsonify, request
from prediction import predict
import os
import json

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def flask_app():
	app = Flask(__name__)

	@app.route('/', methods=['GET'])
	def server_is_up():
		return 'Server is up and running! Nice work! \n'

	@app.route('/predict_mpg', methods=['POST'])
	def mpg():
		to_predict = request.json
		print(to_predict)
		prediction = predict(to_predict)
		return jsonify({"predicted mpg:":prediction})
	return app


if __name__ == '__main__':
	app = flask_app()
	app.run(debug=True, host='0.0.0.0')
