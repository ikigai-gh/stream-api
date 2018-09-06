import json
import time
from elastic_config import elastic_client, INDEX_NAME, DOC_TYPE
from elasticsearch import exceptions
from stream_helper import SEARCH_MATCH_ALL

def add_stream(stream):
	if elastic_client.exists(index = INDEX_NAME, doc_type = INDEX_NAME, id = stream['uuid']):
		return "document already exists"		
	command_result = elastic_client.index(index = INDEX_NAME, doc_type = INDEX_NAME, body = stream, id = stream['uuid'])
	return command_result["result"]		
	
def get_stream(stream_id):
	try:
		stream = elastic_client.get_source(index = INDEX_NAME, doc_type = INDEX_NAME, id = stream_id)
	except exceptions.NotFoundError as e:
		return None
	return stream

def get_all_streams():
	streams = []
	hits = elastic_client.search(index = INDEX_NAME, doc_type = INDEX_NAME, body = SEARCH_MATCH_ALL, size = 10000)['hits']['hits']
	for hit in hits:
		streams.append(hit['_source'])
	return streams

def delete_stream(stream_id):
	if not elastic_client.exists(index = INDEX_NAME, doc_type = INDEX_NAME, id = stream_id):
		return "stream doesn't exist"
	command_result = elastic_client.delete(index = INDEX_NAME, doc_type = INDEX_NAME, id = stream_id)
	return command_result

def update_stream(stream):
	if not elastic_client.exists(index = INDEX_NAME, doc_type = INDEX_NAME, id = stream['uuid']):
		return "stream doesn't exist"
	command_result = elastic_client.index(index = INDEX_NAME, doc_type = INDEX_NAME, body = stream, id = stream['uuid'])
	return command_result["result"]

def import_streams(streams):
	streams_added = 0
	streams_dublicates = 0
	for stream in streams:
		result = add_stream(stream)
		if result == "created":
			streams_added += 1
		elif result == "document already exists":
			streams_dublicates += 1
	command_result = "{}/{} streams were uploaded. Dublicates were ignored".format(streams_added, streams_dublicates) 
	return command_result

def export_streams():
	streams = get_all_streams()
	filename = "{}_streams.json".format(time.time())
	try:
		with open(filename, 'w') as dist:
			json.dump(streams, dist)	
	except Exception as e:
		command_result = "An error occured during the dump"
	command_result = "Dump successfull"	

	return command_result