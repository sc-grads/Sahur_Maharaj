import sys
from flask import jsonify, request, session

sys.path.append('..')
from Modules.DatabaseMod import Connector

dbm = Connector()


def loginEndpoint():
    user = request.json.get('User')
    password = request.json.get('Password')

    dbm.connect()
    dbmUser = dbm.select('employee', ['e_id', 'e_email', 'e_hashpassword', 'e_type'], 'e_email', user, 'e_hashpassword',
                         password)

    if dbmUser:
        userStatus = dbmUser[0][3]
        userid = dbmUser[0][0]

        session['user_id'] = userid  # Store user ID in the session

        response = {
            'status': 200,
            'message': 'Login Successful',
            'data': {
                'userid': userid,
                'userStatus': userStatus
            }
        }
        status_code = 200
    else:
        response = {
            'status': 401,
            'message': 'Invalid Username or Password',
            'data': None
        }
        status_code = 401

    dbm.close()
    return jsonify(response), status_code
