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
    firstname = request.json.get('firstname')
    lastname = request.json.get('lastname')
    wemail = request.json.get('wemail')
    password = request.json.get('password')
    etype = request.json.get('etype')
    print(firstname, lastname, wemail, password, etype)
    # connecting and inserting the data to the db
    try:
        database.connect()
        database.insert('employee', [firstname, lastname, wemail, password, etype])
        database.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': f'Error: {e}'})


# login user
@app.route('/endpoint/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # database operations
    try:
        database.connect()
        database_uname = database.select(table_name='employee',
                                         columns=['e_email'],
                                         where_clause='e_email = ? AND e_hashpassword = ?',
                                         parameters=(username, password))
        database_upass = database.select(table_name='employee',
                                         columns=['e_hashpassword'],
                                         where_clause='e_email = ? AND e_hashpassword = ?',
                                         parameters=(username, password))
        database_uAL = database.select(table_name='employee',
                                       columns=['e_type'],
                                       where_clause='e_email = ? AND e_hashpassword = ?',
                                       parameters=(username, password))
        print(database_uname)
        print(database_upass)
        print(database_uAL)

        # verify login data
        if database_uname[0][0] == username and database_upass[0][0] == password:
            access_level = database_uAL[0][0]
            return jsonify({'status': 'success', 'access_level': access_level}) # include access_level in the response
        else:
            return jsonify({'status': 'error', 'message': 'Invalid credentials'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': f'Error: User Not Found'})


# get user data
@app.route('/endpoint/login/<user>', methods=['POST', 'GET'])
def user_profile():
    pass


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
