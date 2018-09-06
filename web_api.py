import json
from flask import Flask, request, Response
import stream_api
from stream_helper import *

app = Flask(__name__)

@app.route('/api/add_stream', methods=['PUT'])
def add_stream():
	try:
		stream = request.get_json()
	except Exception as e:
		response = Response(json.dumps(STREAM_JSON_PARSE_ERROR), status = 400)
		return response
	
	command_result = (stream_api.add_stream(stream))

	if command_result == "created":
		response = Response(json.dumps(STREAM_ADD_SUCCESS), status = 201)
	elif command_result == "document already exists":
		response = Response(json.dumps(STREAM_ADD_STREAM_ALREADY_EXISTS_ERROR), status = 400)
	return response

@app.route('/api/get_stream', methods=['GET'])
def get_stream():
	stream_id = request.args.get('stream_id')
	stream = stream_api.get_stream(stream_id)

	if stream != None:
		response = Response(json.dumps(stream), status = 200)
	else:
		response = Response(json.dumps(STREAM_DOES_NOT_EXIST_ERROR), status = 404)
	return response

@app.route('/api/get_all_streams', methods=['GET'])
def get_all_streams():
	streams = stream_api.get_all_streams()
	response = Response(json.dumps(streams))
	return response

@app.route('/api/delete_stream', methods=['DELETE'])
def delete_stream():
	stream_id = request.json['stream_id']
	command_result = stream_api.delete_stream(stream_id)

	if command_result == "stream doesn't exist":
		response = Response(json.dumps(STREAM_DOES_NOT_EXIST_ERROR), status = 404)
	else:
		response = Response(json.dumps(STREAM_DELETE_SUCCESS), status = 200)
	return response

@app.route('/api/update_stream', methods=['POST'])
def update_stream():
	try:
		stream = request.get_json()
	except Exception as e:
		response = Response(json.dumps(STREAM_JSON_PARSE_ERROR), status = 400)
		return response
	
	command_result = (stream_api.update_stream(stream))

	if command_result == "updated":
		response = Response(json.dumps(STREAM_UPDATE_SUCCESS), status = 201)
	elif command_result == "stream doesn't exist":
		response = Response(json.dumps(STREAM_DOES_NOT_EXIST_ERROR), status = 404)
	return response

@app.route('/api/import_streams', methods=['PUT'])
def import_streams():
	try:
		streams = request.get_json()
	except Exception as e:
		response = Response(json.dumps(STREAM_JSON_PARSE_ERROR), status = 400)
		return response
	command_result = stream_api.import_streams(streams)
	response = Response(json.dumps(command_result))
	return response

@app.route('/api/export_streams', methods=['GET'])
def export_streams():
	command_result = stream_api.export_streams()
	response = Response(json.dumps(command_result))
	return response