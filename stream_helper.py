STREAM_ADD_SUCCESS = {"Message": "Stream was added successfully"}
STREAM_ADD_STREAM_ALREADY_EXISTS_ERROR = {"Message": "Stream already exists"}
STREAM_GET_STREAM_DOES_NOT_EXIST_ERROR = {"Message": "Stream doesn't exist"}

def construct_stream_from_json(json):
	stream = { "id": json["id"], "title": json["title"], "date": json["date"], "game": json["game"], "url": json["url"] }
	return stream

def decode_redis_response(redis_response):
	if redis_response != None:
		return redis_response.decode('utf-8')
	else:
		return None