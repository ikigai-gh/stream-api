import os
from web_api import app

def start_app():
	host = os.environ.get('IP', '127.0.0.1')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port)

start_app() 