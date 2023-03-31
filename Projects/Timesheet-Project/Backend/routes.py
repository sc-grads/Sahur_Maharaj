# imports
from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD
from Database_manager import manager
=======
>>>>>>> 6a54678b6e4917cffaca909a201ab0919a9156bc

# creating flask class and routing endpoints
app = Flask(__name__)
CORS(app)


# login endpoint
@app.route('/endpoint/login')
def user_login():
<<<<<<< HEAD
    manager.Manager.query('USE ChronoSync; SELECT * FROM employee')
=======
    pass
>>>>>>> 6a54678b6e4917cffaca909a201ab0919a9156bc


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
