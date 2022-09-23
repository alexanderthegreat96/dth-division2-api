import waitress
from main import app
from classes.ApiConfig import ApiConfig

config = ApiConfig()
waitress.serve(app, host=''+config.api_host+'', port=config.api_port)