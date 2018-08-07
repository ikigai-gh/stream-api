import json
from flask import Flask, request
import stream_api

app = Flask(__name__)

# TODO: Add correct HTTP responses with the result of redis operation
# TODO: Add json serialization/deserialization

@app.route('/api/add_stream', methods=['PUT'])
def add_stream(stream):
	command_result = stream_api.add_stream(stream)
	return command_result

@app.route('/api/get_stream', methods=['GET'])
def get_stream(stream_id):
	command_result = stream_api.get_stream(stream)
	return command_result

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