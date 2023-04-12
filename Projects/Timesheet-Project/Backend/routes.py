# imports
import base64
import hashlib
from flask import Flask, jsonify, request
import json
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
    data = request.get_json()

    fname = data['fname']
    lname = data['lname']
    email = data['email']
    password = data['passwd']
    salt = data['salt']
    emp_type = data['selectedT']
    # add user data to database
    try:
        database.connect()
        database.insert('employee', [fname, lname, email, password, salt, emp_type])
        database.close()
    except Exception as e:
        print(e)
        response = {'error': 'Could not register user'}
        return jsonify(response), 500

    # Return a JSON response
    response = {'success': 'OK'}
    return response


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
