# imports
from flask import Flask, jsonify, request

from flask_cors import CORS
from database_manager.manager import Manager

# creating flask class and routing endpoints
app = Flask(__name__)
CORS(app, resources={r"/endpoint/*": {"origins": "http://localhost:4200"}})

database = Manager(server_name='localhost',
                   database_name='ChronoSync',
                   database_user='api',
                   database_userpass='Qwerty1!')


# register endpoint
@app.route('/endpoint/register', methods=['POST'])
def register_user():
    pass


# loging user in
@app.route('/endpoint/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    print(username, password)
    if username == 'test' and password == 'test':
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'})


# get user data
@app.route('/endpoint/login/<user>', methods=['POST', 'GET'])
def user_profile():
    pass


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
