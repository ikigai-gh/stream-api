import json
from flask import Flask, request
import stream_api

app = Flask(__name__)

# TODO: Add extended information about errors in responses

@app.route('/api/add_stream', methods=['PUT'])
def add_stream():
	stream = construct_stream_from_json(request.json)
	command_result = decode_redis_response(stream_api.add_stream(stream))
	if command_result != None:
		response = Response(json.dumps(STREAM_ADD_SUCCESS), status = 200)
	else:
		response = Response(json.dumps(STREAM_ADD_STREAM_ALREADY_EXISTS_ERROR), status = 400)
	return response

@app.route('/api/get_stream', methods=['GET'])
def get_stream():
	stream_id = request.args.get('stream_id')
	stream = decode_redis_response(stream_api.get_stream(stream_id))
	if stream != None:
		response = Response(stream, status = 200)
	else:
		response = Response(json.dumps(STREAM_GET_STREAM_DOES_NOT_EXIST_ERROR), status = 404)
	return response

@app.route('/api/get_all_streams', methods=['GET'])
def get_all_streams():
	command_result = stream_api.get_all_streams(stream)
	return command_result

@app.route('/api/delete_stream', methods=['DELETE'])
def delete_stream(stream_id):
	command_result = stream_api.delete_stream(stream)
	return command_result

@app.route('/api/update_stream', methods=['POST'])
def update_stream(stream):
	command_result = stream_api.update_stream(stream)
	return command_result

@app.route('/api/dump_streams', methods=['GET'])
def dump_streams():
	command_result = stream_api.dump_streams(stream)
	return command_result 