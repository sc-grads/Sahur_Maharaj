from flask import Flask, request, jsonify, render_template, abort
import jwt
from flask_cors import CORS
import db_manager as db

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    uname = data.get('username')
    passwd = data.get('password')
    print(uname)
    print(passwd)
    if db.login(uname, passwd):
        return jsonify(data)
    else:
        return '404'


if __name__ == '__main__':
    app.run(debug=True)
