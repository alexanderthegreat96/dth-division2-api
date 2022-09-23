import json
from flask import Flask
from flask import Response
from flask import request
from classes.Authenticate import AuthenticateRequest
from waitress import serve
from classes.DatabaseWrapper import DatabaseWrapper
from classes.ChromeBrowser import ChromeBrowser
from classes.DataGrabber import Datagrabber
from classes.ApiLogger import ApiLogger
from classes.ApiConfig import ApiConfig

config = ApiConfig()
chrome = ChromeBrowser()

app = Flask(__name__)

# limiter = Limiter(app, key_func=get_remote_address,storage_uri="memcached://localhost:11211",
#     storage_options={})

@app.route('/api/', methods=['GET'])
def home():
    return Response(
        json.dumps(
            {
                'status': True,
                'message': 'Welcome! This is the Division2 API built by alexanderdth. Reffer to /api/help, to learn how to use the api.'
            }),
        status=200,
        mimetype='application/json')


@app.route('/api/help', methods=['GET'])
def help():
    return Response(
        json.dumps(
            {
                'status': True,
                'message':
                    [
                        {
                            'endpoint': '/api/query-data',
                            'platforms': ['xbox', 'psn', 'uplay'],
                            'method': 'POST',
                            'required': [{'api_key': '<your-api-key>', 'username': 'platform_username',
                                          'platform': 'your_platform'}]
                        },
                        {
                            'endpoint': '/api/help',
                            'method': 'GET',
                        },
                        {
                            'endpoint': '/api/',
                            'method': 'GET'
                        }
                    ]
            }),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/query-data', methods=['POST'])

#@limiter.limit(str(config.rate_limiting)+"/minute")

def query_data():
    username = request.form.get('username')
    api_key = request.form.get('api_key')
    platform = request.form.get('platform')

    if (username and api_key and platform):
        authenticateRequest = AuthenticateRequest()
        auth = authenticateRequest.authenticate(api_key)
        logger = ApiLogger()

        if (auth == 'authenticated'):

            grabber = Datagrabber(username, platform, chrome)
            data = grabber.fetchPlayerData()

            if ('error' not in data):

                logger.logData(api_key, '/api/query-data', 'POST', json.dumps(data))

                return Response(
                    json.dumps({
                        'status': True,
                        'data': data['data']
                    }),
                    status=200,
                    mimetype='application/json'
                )
            else:
                logger.logData(api_key, '/api/query-data', 'POST', json.dumps(data))

                return Response(
                    json.dumps({
                        'status': False,
                        'error': data['error']
                    }),
                    status=404,
                    mimetype='application/json'
                )
        else:
            logger.logData(api_key, '/api/query-data', 'POST',
                           json.dumps({'error': 'Your API key is not authorized to access the system.'}))

            return Response(
                json.dumps(
                    {
                        'status': False,
                        'error': 'Your API key is not authorized to access the system.'
                    }), status=403, mimetype='application/json')
    else:
        return Response(
            json.dumps(
                {
                    'status': False,
                    'error': 'You have missing parameters in your request. Make sure you provide username,api_key and platform'
                }), status=500, mimetype='application/json')

@app.errorhandler(429)
def ratelimit_handler(e):
  return Response(json.dumps({'status': False,'error' : 'You are rate limited. Too many requests per minute.'}),status=500, mimetype='application/json')

# app.run(host=''+config.api_host+'', port=config.api_port)