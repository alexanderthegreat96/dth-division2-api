requirements : python3.8+

installation:
create a database and import the sql file
edit config.json and set your mysql params
use a mysql client to append api keys into users

Run these 2 commands:

python3 -m pip install -r requiements.py
python3 server.py / or waitress-serve --host 0.0.0.0 --port=105 main:app



head over to localhost:105/api/help to check the available endpoints
Use postman to send data to the api and to check error mappins

api key: JaRyk3ys4fVZrwHzMAba

