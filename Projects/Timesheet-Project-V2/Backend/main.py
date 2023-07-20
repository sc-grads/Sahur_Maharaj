from flask import Flask, request, jsonify
from flask_cors import CORS

from Controllers import *
from Models import *
import jwt


class TimesheetApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.cors = CORS(self.app, origins=['http://localhost:4200'])
        self.app.secret_key = 'addmetoenvvars'

        self.setup_routes()

    def setup_routes(self):
        self.app.route('/endpoint/login', methods=['POST'])(self.login)
        self.app.route('/endpoint/load', methods=['GET'])(self.load)
        self.app.route('/endpoint/clockentry', methods=['POST'])(self.clock)
        self.app.route('/endpoint/editsheetentry', methods=['POST'])(self.edit)

    def run(self):
        self.app.run(debug=True)

    def login(self):
        user_data = request.json
        username = user_data.get('User')
        password = user_data.get('Password')
        print(user_data)
        is_logged_in = LoginController.Login().validate(username, password)
        print(is_logged_in)
        if is_logged_in:
            user = User.User.get_user()
            if user.get_email() != username:
                User.User.clear_user_list()

            payload = {
                'userid': user.get_id(),
                'username': user.get_email(),
                'password': user.get_hashpassword(),
                'usertype': user.get_etype(),
            }
            token = jwt.encode(payload, self.app.secret_key, algorithm='HS256')
            response = {
                'token': token,
                'message': 'User Logged in Successfully'
            }
            return response, 200
        else:
            response = {
                'token': None,
                'message': 'Incorrect Username or password'
            }
            return response, 401

    def load(self):
        user = User.User.get_user()
        #print(user)
        if user:
            load_ctrl = LoadController.Load()
            userid = user.get_id()
            print(userid)
            return jsonify({
                'userid': userid,
                'userName': user.get_name(),
                'clients': load_ctrl.load_clients(),
                'tasks': load_ctrl.load_tasks(),
                'timesheet': load_ctrl.load_timesheet(userid),
                'message': 'Loaded'
            }), 200
        else:
            response = {
                'message': 'User not found'
            }
            return response, 401

    def clock(self):
        clock_data = request.json
        userid = clock_data.get('userid')
        date = clock_data.get('date')
        billable = clock_data.get('billable')
        project = clock_data.get('project')
        client = clock_data.get('client')
        task = clock_data.get('task')
        comment = clock_data.get('comment')
        s_time = clock_data.get('startTime')
        e_time = clock_data.get('endTime')
        spenttime = clock_data.get('spentTime')

        clock_controller = ClockController.Clock()
        clock_controller.insert_clock(date, billable, project, userid, client, task, comment, s_time, e_time, spenttime)

        return {'message': 'Inserted Clock'}

    def edit(self):
        edited = request.json
        sheet_id = edited.get('entry_no')  # Assuming 'entry_no' represents the sheet ID
        update_timesheet = EditController.UpdateTimeSheet() # Create an instance of the UpdateTimeSheet class
        update_timesheet.update_timesheet(edited.get('client_name'),edited.get('task_name'),
                                          sheet_id, edited.get('billable'), edited.get('project'),
                                          edited.get('comment'), edited.get('start_time'), edited.get('end_time'),
                                          edited.get('time_spent'))

        return {'message': 'Timesheet entry updated'}, 200


if __name__ == '__main__':
    app = TimesheetApp()
    app.run()
