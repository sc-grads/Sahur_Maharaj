import sys
sys.path.append("..")
from Modules.DatabaseMod import Connector

class Loader:

    def __init__(self):
        self.dbm = Connector()

    def load_clients(self):
        self.dbm.connect()
        return self.dbm.select('client', '*', None, None, None, None)

    def load_tasks(self):
        self.dbm.connect()
        return self.dbm.select('task', '*', None, None, None, None)

    def load_timesheet(self, user_id):
        self.dbm.connect()
        return self.dbm.select('employee_timesheet', '*', 'employee_id', user_id, None, None)
