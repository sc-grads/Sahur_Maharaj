import sys
sys.path.append("..")
from Modules.DatabaseMod import Connector

class Loader:

    def __init__(self):
        self.dbm = Connector()

    def load_clients(self):
        self.dbm.connect()
        clients = self.dbm.select('client', '*', None, None, None, None)
        self.dbm.close()
        return clients

    def load_tasks(self):
        self.dbm.connect()
        tasks = self.dbm.select('task', '*', None, None, None, None)
        self.dbm.close()
        return tasks

    def load_timesheet(self, user_id):
        self.dbm.connect()
        timesheet = self.dbm.select('timesheet', '*', 'employee_id', user_id, None, None)
        self.dbm.close()
        return timesheet
