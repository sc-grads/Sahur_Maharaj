# imports
from flask import Flask
from flask_cors import CORS

# creating flask class and routing endpoints
app = Flask(__name__)
CORS(app)


# login endpoint
@app.route('/endpoint/login')
def user_login():
    pass


if __name__ == '__main__':
    print('Running Flask Endpoint server')
    app.run(debug=True)
