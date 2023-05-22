import sys

sys.path.append('..')
from Modules.loadMod import Loader
from flask import jsonify, request

loader = Loader()

print(loader.load_timesheet(1))


def loadendpoint():
    userid = request.json.get('EmployeeID')
    load_tasks = loader.load_tasks()
    load_clients = loader.load_clients()
    load_timesheet = loader.load_timesheet(userid)

    return jsonify({'message': 'All data sent', 'Data': {
        'clients': load_clients,
        'tasks': load_tasks,
        'timesheet': load_timesheet}
                    }), 200
