import sys

sys.path.append('..')
from Modules.loadMod import Loader
from flask import jsonify

loader = Loader()


def loadendpoint(user_id):
    load_tasks = loader.load_tasks()
    load_clients = loader.load_clients()
    load_timesheet = loader.load_timesheet(user_id)
    print(load_timesheet)

    timesheet = [
        {
            'empID': times[0],
            'sheetID':times[1],
            'totaltime':times[2]
        }
        for times in load_timesheet
    ]

    tasks = [
        {
            'id': task[0],
            'Name': task[1],
            'Description': task[2]
        }
        for task in load_tasks
    ]

    clients = [
        {
            'id': client[0],
            'Name': client[1],
            'Description': client[2]
        }
        for client in load_clients
    ]


    response = {
        'status': 200,
        'message': f'Data sent for user ID {user_id}',
        'data': {
            'clients': clients,
            'tasks': tasks,
            'timesheet': timesheet
        }
    }

    return jsonify(response), 200
