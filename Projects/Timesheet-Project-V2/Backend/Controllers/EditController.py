import sys
sys.path.append('..')
from Modules import DatabaseModule

class UpdateTimeSheet:
    def __init__(self):
        self.dbm = DatabaseModule.DatabaseManager()

    def update_timesheet(self, client_name, task_name, sheet_id, billable, project, comment, st, et, sptt):
        client_id = self.dbm.select_data('client', ['c_id'], WHERE='c_name = ?', params=[client_name])
        task_id = self.dbm.select_data('task', ['t_id'], WHERE='t_name = ?', params=[task_name])

        if billable.lower() == 'yes':
            billable = 'true'
        else:
            billable = 'false'

        edited_data = {
            't_billable': billable,
            't_project': project,
            'client_id': client_id[0][0] if client_id else None,
            'task_id': task_id[0][0] if task_id else None,
            't_comment': comment,
            't_start': st,
            't_end': et,
            't_spent': sptt
        }

        condition = f"t_id = {sheet_id}"
        self.dbm.update_data('timesheet', edited_data, condition)
