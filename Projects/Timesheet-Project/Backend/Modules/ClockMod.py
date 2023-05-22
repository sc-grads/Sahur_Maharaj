import sys
sys.path.append("..")
from Modules.DatabaseMod import Connector


class Clock:

    def __init__(self):
        self.dbm = Connector()

    def insert_clock(self, table, cols, vals):
        return self.dbm.insert(table, cols, vals)