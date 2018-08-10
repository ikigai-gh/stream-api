import json
from redis_config import redis_client

def add_stream(stream):
	command_result = redis_client.execute_command('JSON.SET', stream["id"], '.', json.dumps(stream), 'NX')
	return command_result

def get_stream(stream_id):
	stream = redis_client.execute_command('JSON.GET', stream_id)
	return stream

def get_all_streams():
	# ...
	command_result

def delete_stream(stream_id):
	command_result = redis_client.execute_command('JSON.DEL', stream_id)
	return command_result

def update_stream(stream):
	stream_ = json.loads(redis_client.execute_command('JSON.GET', stream_id))
	command_result = redis_client.execute_command('JSON.SET', stream.id, '.', json.dumps(stream))
	return command_result

def dump_streams():
	command_result = redis_client.bgsave()
	return command_result