# import pyodbc library for interacting with the database
import pyodbc

# Creating database manager class
class Manager:
    def __init__(self, server_name, database_name, database_user, database_userpass):
        # initialize class variables
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
            # establish connection to the database
            self.con = pyodbc.connect(f'Driver={self.driver};'
                                      f'Server={self.server};'
                                      f'Database={self.database};'
                                      f'UID={self.user};'
                                      f'PWD={self.passwd};')
            # create cursor object to execute queries
            self.cursor = self.con.cursor()
            # print(f'Connected to database {self.con.getinfo(pyodbc.SQL_DATABASE_NAME)}')
        except Exception as error:
            # if there's an exception, print the error message and raise it
            print(f'An Exception has occurred with error code: {error}')
            raise error

    # insert into the DB
    def insert(self, table_name, values):
        # join all the values with commas and wrap them in quotes
        values_str = ', '.join([f"'{v}'" for v in values])
        # create SQL query to insert data into the table
        query = f"INSERT INTO {table_name} VALUES ({values_str})"
        # execute the query
        self.cursor.execute(query)
        # commit the changes to the database
        self.con.commit()
        print('Inserted')

    # select from the database
    def select(self, table_name, columns=None, where_clause=None, parameters=None):
        # if no columns specified, select all columns
        if columns is None:
            select_clause = "*"
        else:
            # join the columns with commas
            select_clause = ", ".join(columns)

        # if no where clause specified, select all rows
        if where_clause is None:
            query = f"SELECT {select_clause} FROM {table_name}"
        else:
            # create SQL query with where clause
            query = f"SELECT {select_clause} FROM {table_name} WHERE {where_clause}"

        # if there are parameters to be passed in, execute query with parameters
        if parameters is not None:
            self.cursor.execute(query, parameters)
        else:
            # otherwise, execute query without parameters
            self.cursor.execute(query)

        # fetch all the rows returned by the query
        rows = self.cursor.fetchall()
        # return the rows
        return rows

    # closing connection
    def close(self):
        # if the cursor is not none, close the cursor
        if self.cursor:
            self.cursor.close()
        # if the connection is not none, close the connection
        if self.con:
            self.con.close()


# running the module
if __name__ == '__main__':
    # print the module name
    print(__name__)

    # create a new database manager object
    print('Running Database_Manager Module')
    database = Manager(server_name='localhost',
                       database_name='ChronoSync',
                       database_user='api',
                       database_userpass='Qwerty1!')
    # connect to the database
    database.connect()
    # close the connection
    database.close()
