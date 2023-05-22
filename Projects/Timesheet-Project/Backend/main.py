from flask import Flask, request
from flask_cors import CORS
from Controllers import *

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'], supports_credentials=True)


@app.route('/endpoint/login', methods=['POST'])
def login():
    return LoginController.loginEndpoint()


@app.route('/endpoint/loaduserid=<int:user_id>', methods=['GET', 'POST'])
def load_data(user_id):
    print(f'Sent Load for {user_id}')
    return LoadController.loadendpoint(user_id)


@app.route('/endpoint/clockentry', methods=['POST'])
def clock():
    return ClockController.Clockendpoint()


if __name__ == '__main__':
    app.run(debug=True)
