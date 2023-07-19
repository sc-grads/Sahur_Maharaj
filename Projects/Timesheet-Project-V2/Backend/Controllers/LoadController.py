# imports
import sys

sys.path.append('..')
from Modules import DatabaseModule
from Models.Client import Client
from Models.Task import Task
from Models.User import User
from Models.TImesheet import Timesheet


class Load:
    def __init__(self):
        self.dbm = DatabaseModule.DatabaseManager()

    def load_clients(self):
        Client.empty_client_list()
        client_data = self.dbm.select_data('client', ['c_id', 'c_name', 'c_notes'])
        client_list = [
            [client_info[0], client_info[1], client_info[2]]
            for client_info in client_data
        ]
        for client in client_list:
            Client.add_client(client)
        print('Loaded Clients')

        clients = Client.get_client_list()
        json_clients = [
            {
                'id': client[0],
                'Name': client[1],
                'Description': client[2]
            }
            for client in clients
        ]

        return json_clients

    def load_tasks(self):
        Task.empty_task_list()
        task_data = self.dbm.select_data('task', ['t_id', 't_name', 't_description'])
        Task.task_list = [
            [task_info[0], task_info[1], task_info[2]]
            for task_info in task_data
        ]
        print('Loaded Tasks')
        json_tasks = [
            {
                'id': task[0],
                'Name': task[1],
                'Description': task[2]
            }
            for task in Task.task_list
        ]
        return json_tasks

    def load_timesheet(self, user_id):
        Timesheet.empty_timesheet_list()
        timesheet_data = self.dbm.select_data('timesheet', WHERE='employee_id = ?', params=[user_id])
        timesheet_list = [
            [timesheet_info[0], timesheet_info[1], timesheet_info[2], timesheet_info[3], timesheet_info[4],
             timesheet_info[5], timesheet_info[6], timesheet_info[7], timesheet_info[8], timesheet_info[9],
             timesheet_info[10]]
            for timesheet_info in timesheet_data
        ]
        for timesheet in timesheet_list:
            Timesheet.add_timesheet(timesheet)

        timesheets = Timesheet.get_timesheet_list()
        json_timesheets = [
            {
                'entry_no': timesheet[0],
                'date': timesheet[1],
                'billable': timesheet[2],
                'project': timesheet[3],
                'comment': timesheet[4],
                'start_time': timesheet[5],
                'end_time': timesheet[6],
                'time_spent': timesheet[7],
                'user_id': timesheet[8],
                'task_id': timesheet[9],
                'client_id': timesheet[10]
            }
            for timesheet in timesheets
        ]

        return json_timesheets
