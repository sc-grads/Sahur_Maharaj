# imports
import pyodbc


# Creating database manage class
class Manager:
    def __init__(self, server_name, database_name, database_user, database_userpass):
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.server = server_name
        self.database = database_name
        self.user = database_user
        self.passwd = database_userpass
        self.con = None
        self.cursor = None

    # connecting to the database and error handler
    def connect(self):
        try:
            self.con = pyodbc.connect(f'Driver={self.driver};'
                                      f'Server={self.server};'
                                      f'Database={self.database};'
                                      f'UID={self.user};'
                                      f'PWD={self.passwd};')
            self.cursor = self.con.cursor()
            print(f'Connected to database {self.con.getinfo(pyodbc.SQL_DATABASE_NAME)}')
        except Exception as error:
            print(f'An Exception has occurred with error code: {error}')

    # query the DB
    def query(self, query):
        pass

    # closing connection
    def close(self):
        print(f'Closing connection to {self.con.getinfo(pyodbc.SQL_DATABASE_NAME)}')
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()


if __name__ == '__main__':
    print(__name__)
    print('Running...')
    database = Manager(server_name='DESKTOP-OP7DVNI',
                       database_name='ChronoSync',
                       database_user='api',
                       database_userpass='Qwerty1!')
    database.connect()
    database.close()
