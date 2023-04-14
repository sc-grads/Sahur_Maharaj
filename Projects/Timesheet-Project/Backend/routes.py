# imports
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from database_manager.manager import Manager

# creating flask class and routing endpoints
app = Flask(__name__)
app.secret_key = 'move_me'
CORS(app, resources={r"/endpoint/*": {"origins": "http://localhost:4200"}})
# instantiate DB object
database = Manager(server_name='localhost',
                   database_name='ChronoSync',
                   database_user='api',
                   database_userpass='Qwerty1!')


# register endpoint
@app.route('/endpoint/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
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
    else:
        return jsonify({'status': 'error', 'message': f'Error: Incorrect Http Method'})


# login user
@app.route('/endpoint/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # returned variables from response
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
            database_ual = database.select(table_name='employee',
                                           columns=['e_type'],
                                           where_clause='e_email = ? AND e_hashpassword = ?',
                                           parameters=(username, password))

            # verify login data
            if database_uname[0][0] == username and database_upass[0][0] == password:
                access_level = database_ual[0][0]
                # creating user Session
                session['username'] = username
                session['access_level'] = access_level
                # include access_level in the response
                return jsonify({'status': 'success', 'access_level': access_level})
            else:
                return jsonify({'status': 'error', 'message': 'Invalid credentials'})
        except Exception as e:
            print(e)
            return jsonify({'status': 'error', 'message': f'Error: User Not Found'})
    else:
        return jsonify({'status': 'error', 'message': 'Incorrect Http Method'})


# get user data
@app.route('/endpoint/login/<username>', methods=['GET', 'POST'])
def user_profile(username):
    print(username)
    if request.method == 'GET':
        # check if user is logged in
        if 'username' in session:
            # retrieve user data from the database
            try:
                database.connect()
                user_data = database.select(table_name='employee',
                                            columns=['e_firstname', 'e_lastname', 'e_email', 'e_type'],
                                            where_clause='e_email = ?',
                                            parameters=(username,))
                database.close()
                # return user data as JSON response
                return jsonify({'status': 'success',
                                'firstname': user_data[0][0],
                                'lastname': user_data[0][1],
                                'email': user_data[0][2],
                                'access_level': user_data[0][3]})
            except Exception as e:
                print(e)
                return jsonify({'status': 'error', 'message': f'Error: {e}'})
        else:
            return jsonify({'status': 'error', 'message': 'User not logged in'})
    else:
        return jsonify({'status': 'error', 'message': 'User not logged in'})


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
