def construct_stream_from_json(json):
	stream = { "id": json["id"], "title": json["title"], "date": json["date"], "game": json["game"], "url": json["url"] }
	return stream