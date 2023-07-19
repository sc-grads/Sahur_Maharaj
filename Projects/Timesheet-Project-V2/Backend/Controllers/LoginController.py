# imports
import sys
sys.path.append('..')
from Modules import DatabaseModule
from Models import User


class Login:

    def __init__(self):
        self.dbm = DatabaseModule.DatabaseManager()
        self.user = None

    def validate(self, username, password):
        # get data from database
        exists = self.dbm.select_data('employee', ['e_id', 'e_name', 'e_surname', 'e_email', 'e_hashpassword', 'e_type'],
                        WHERE='e_email = ? AND e_hashpassword = ?', params=[username, password])
        if exists:
            self.user = User.User(exists[0][0],exists[0][1],exists[0][2],
                                  exists[0][3],exists[0][4],exists[0][5])
            self.user.add_user()

            return True
        else:
            return False
