from flask import Flask, request, session, jsonify
from flask_cors import CORS
from Controllers import *

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'], supports_credentials=True)

# Set the secret key for session management
app.secret_key = 'your_secret_key_here'

# Configure session options
app.config['SESSION_COOKIE_NAME'] = 'your_session_cookie_name'
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True if using HTTPS


# Login endpoint
@app.route('/endpoint/login', methods=['POST'])
def login():
    return LoginController.loginEndpoint()


# Load data endpoint
@app.route('/endpoint/loaduserid=<int:user_id>', methods=['GET', 'POST'])
def load_data(user_id):
    # Check if the user is logged in before accessing this endpoint
    if 'user_id' not in session:
        return jsonify({'status': 401, 'message': 'Unauthorized', 'data': None}), 401

    return LoadController.loadendpoint(user_id)


# Clock entry endpoint
@app.route('/endpoint/clockentry', methods=['POST'])
def clock():
    # Check if the user is logged in before accessing this endpoint
    if 'user_id' not in session:
        return jsonify({'status': 401, 'message': 'Unauthorized', 'data': None}), 401

    return ClockController.Clockendpoint()


if __name__ == '__main__':
    app.run(debug=True)
