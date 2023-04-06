# imports
from flask import Flask, jsonify
from flask_cors import CORS
from database_manager.manager import Manager

# creating flask class and routing endpoints
app = Flask(__name__)
CORS(app)

database = Manager(server_name='localhost',
                   database_name='ChronoSync',
                   database_user='api',
                   database_userpass='Qwerty1!')


# login endpoint
@app.route('/endpoint/login')
def user_login():
    database.connect()
    result = database.query("SELECT * FROM employee")
    database.close()
    return jsonify(result)


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
