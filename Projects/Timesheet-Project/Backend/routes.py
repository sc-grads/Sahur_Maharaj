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


# login verification against the database
@app.route('/endpoint/login', methods=['POST'])
def validate_login():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        print(email, password)
        # validate the password from the database and return the data to angular
        try:
            # connecting to the database and getting the data
            database.connect()
            employee = database.select('employee', columns=['*'],
                                       where_clause="e_email = ? AND e_hashpassword = ?",
                                       parameters=[email, password])

            # employee variables for session
            employee_id = employee[0][0]
            employee_first_name = employee[0][1]
            employee_last_name = employee[0][2]
            employee_mail = employee[0][3]
            employee_hash = employee[0][4]
            employee_type = employee[0][5]

            # verification if employee exist
            if employee_mail == email and employee_hash == password:
                print(f'Access granted for employee: {employee_first_name} with access level of: {employee_type}')
                # creating a session for the user
                session['id'] = employee_id
                session['fname'] = employee_first_name
                session['lname'] = employee_last_name
                session['mail'] = employee_mail
                session['type'] = employee_type
                # send user to angular
                user_data = {'id': session.get('id'),
                             'fname': session.get('fname'),
                             'lname': session.get('lname'),
                             'mail': session.get('mail'),
                             'type': session.get('type')}
                return jsonify({'message': 'OK', 'Data': user_data})
            else:
                return jsonify({'message': 'User Does not exist', 'data': None})
        except Exception as e:
            return jsonify({'message': 'User Does not exist', 'data': None})
        # close connection
        finally:
            database.close()
    else:
        return jsonify({'message': 'Incorrect Request Method', 'error': 400})


@app.route('/endpoint/load/', methods=['GET'])
def load_data():

    if request.method == 'GET':
        # connect and get client / task from db
        try:
            database.connect()
            client_list = database.select('client', columns=['*'])
            task_list = database.select('task', columns=['*'])
            # create and send dictionaries to angular
            clients = [{'id': c[0], 'name': c[1], 'description': c[2]} for c in client_list]
            tasks = [{'id': t[0], 'name': t[1], 'description': t[2]} for t in task_list]

            print(clients)
            print(tasks)

            return jsonify({'message': 'OK', 'clients': clients, 'tasks': tasks})

        except Exception as e:
            return jsonify({'message': 'User Does not exist', 'data': None})
        # close connection
        finally:
            database.close()
    else:
        return jsonify({'message': 'Incorrect Request Method', 'error': 400})


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
