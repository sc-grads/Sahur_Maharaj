import sys

sys.path.append('..')
from Modules.DatabaseMod import Connector
from flask import jsonify, request

dbm = Connector()


def Clockendpoint():
    clock_data = request.json
    data = clock_data['data']
    data_variables = {
        'userId': None,
        'date': None,
        'billable': None,
        'project': None,
        'client': None,
        'task': None,
        'startTime': None,
        'endTime': None,
        'spentTime': None,
        'comment': None
    }

    for key, value in data.items():
        if key in data_variables:
            data_variables[key] = value

    d_userId = data_variables['userId']
    d_date = data_variables['date']
    d_billable = data_variables['billable']
    d_project = data_variables['project']
    d_client = data_variables['client']
    d_task = data_variables['task']
    d_startTime = data_variables['startTime']
    d_endTime = data_variables['endTime']
    d_spentTime = data_variables['spentTime']
    d_comment = data_variables['comment']

    dbm.connect()
    task_id = dbm.select('task', ['t_id'], 't_name', d_task, None, None)[0][0]
    client_id = dbm.select('client', ['c_id'], 'c_name', d_client, None, None)[0][0]

    ts_cols = ['t_date', 't_billable', 't_project', 't_comment', 't_start', 't_end', 't_spent', 'employee_id',
               'task_id',
               'client_id']
    ts_vals = [d_date, f'{d_billable}', d_project, d_comment, d_startTime, d_endTime, d_spentTime, d_userId, task_id,
               client_id]

    dbm.insert('timesheet', ts_cols, ts_vals)
    dbm.close()

    return jsonify({'status': 200, 'message': 'Page got data', 'data': None}), 200
