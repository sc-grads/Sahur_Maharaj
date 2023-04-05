# imports
from flask import Flask
from flask_cors import CORS
from Database_manager import manager

# creating flask class and routing endpoints
app = Flask(__name__)
CORS(app)


# login endpoint
@app.route('/endpoint/login')
def user_login():
    manager.Manager.query('USE ChronoSync; SELECT * FROM employee')

    pass


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
