import sys

sys.path.append('..')
from Modules.DatabaseMod import Connector
from flask import jsonify, request
from Modules.ClockMod import Clock

dbm = Connector()

def Clockendpoint():
    clock_data = request.json
    print(clock_data)
    return '', 200