# imports
from flask import Flask, jsonify, request
from flask import session
from flask_cors import CORS
from database_manager.manager import Manager

# creating flask class and routing endpoints
app = Flask(__name__)
app.secret_key = 'dddrsgsed'

CORS(app, resources={r"/endpoint/*": {"origins": "http://localhost:4200"}})
# instantiate DB object
database = Manager(server_name='localhost',
                   database_name='ChronoSync',
                   database_user='api',
                   database_userpass='Qwerty1!')



if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
