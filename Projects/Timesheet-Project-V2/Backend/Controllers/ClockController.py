# imports
import sys

sys.path.append('..')
from Modules import DatabaseModule


class Clock:
    def __init__(self):
        self.dbm = DatabaseModule.DatabaseManager()

    def insert_clock(self, date, billable, project,
                     userid, client, task, comment,
                     starttime, endtime, spenttime):
        # Retrieve the client ID
        client_rows = self.dbm.select_data('client', columns=['c_id'], WHERE='c_name = ?', params=[client])
        if client_rows:
            client_id = client_rows[0][0]
        else:
            print(f'Client "{client}" not found.')
            return

        # Retrieve the task ID
        task_rows = self.dbm.select_data('task', columns=['t_id'], WHERE='t_name = ?', params=[task])
        if task_rows:
            task_id = task_rows[0][0]
        else:
            print(f'Task "{task}" not found.')
            return

        # Prepare the clock data as a dictionary
        clock_data = {
            't_date': date,
            't_billable': billable,
            't_project': project,
            't_comment': comment,
            't_start': starttime,
            't_end': endtime,
            't_spent': spenttime,
            'employee_id': userid,
            'task_id': task_id,
            'client_id': client_id
        }

        # Insert the clock data into the database
        self.dbm.insert_data('timesheet', clock_data)
