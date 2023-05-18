from flask import Flask
from flask_cors import CORS
from Controllers import *

app = Flask(__name__)
CORS(app)


@app.route('/endpoint/login', methods=['POST'])
def login():
    return LoginController.loginEndpoint()


if __name__ == '__main__':
    app.run(debug=True)
