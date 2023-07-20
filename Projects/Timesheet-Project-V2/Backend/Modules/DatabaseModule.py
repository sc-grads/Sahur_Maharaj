import pyodbc


class DatabaseManager:
    def __init__(self):
        self.__server = 'localhost'
        self.__database = 'ChronoSync'
        self.__user = 'api'
        self.__passwd = 'Qwerty1!'
        self.__connection = None
        self.__cursor = None

    def __open_connect(self):
        try:
            # Build connection string
            conn_str = f'DRIVER={{SQL Server}};' \
                       f'SERVER={self.__server};' \
                       f'DATABASE={self.__database};' \
                       f'UID={self.__user};' \
                       f'PWD={self.__passwd}'

            # Establish the database connection
            self.__connection = pyodbc.connect(conn_str)
            self.__cursor = self.__connection.cursor()
        except pyodbc.Error as e:
            # Connection error occurred
            print(f'Connection error {e}')
        finally:
            # Print a separator line
            print(f'Connection to: {self.__connection.getinfo(pyodbc.SQL_DATABASE_NAME)} is Open')
            print('-' * 50)

    def __close_connection(self):
        if self.__connection:
            # Close the database connection if it is open
            print(f'Connection to {self.__connection.getinfo(pyodbc.SQL_DATABASE_NAME)} is now closed.')
            self.__connection.close()
            print('-' * 50)
        else:
            print('Connection was not closed')
            print('*' * 50)

    def select_data(self, table, columns=None, **kwargs):
        try:
            self.__open_connect()

            if columns is None:
                columns = '*'
            else:
                columns = ', '.join(columns)
            query = f"SELECT {columns} FROM {table}"

            if 'WHERE' in kwargs:
                where_conditions = kwargs['WHERE']
                query += f" WHERE {where_conditions}"

            if 'JOIN' in kwargs:
                join_statements = kwargs['JOIN']
                query += f" {join_statements}"

            self.__cursor.execute(query, kwargs.get('params', []))
            rows = self.__cursor.fetchall()

            return rows
        except pyodbc.Error as select_err:
            print(f'Error in Select {select_err}')
            print('*' * 50)
        finally:
            print(f'Selection from {table} is complete')
            print('-' * 50)
            self.__cursor.close()
            self.__close_connection()

    def insert_data(self, table, data):
        try:
            self.__open_connect()

            columns = ', '.join(data.keys())
            values = ', '.join(['?' for _ in range(len(data))])
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            self.__cursor.execute(query, tuple(data.values()))
            self.__connection.commit()
            print(f"Data inserted into {table} successfully.")
        except pyodbc.Error as insert_err:
            print(f'Error in Insert {insert_err}')
            print('*' * 50)
            self.__connection.rollback()
        finally:
            self.__close_connection()

    def update_data(self, table, data, condition):
        try:
            self.__open_connect()

            set_clause = ', '.join([f"{column} = ?" for column in data.keys()])
            query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
            self.__cursor.execute(query, tuple(data.values()))
            self.__connection.commit()
            print(f"Data updated in {table} successfully.")
        except pyodbc.Error as update_err:
            print(f'Error in Update {update_err}')
            print('*' * 50)
            self.__connection.rollback()
        finally:
            self.__close_connection()

# dbm = DatabaseManager()
# rows = dbm.select_data('employee', ['e_id', 'e_name', 'e_type'], WHERE='e_id = ?', params=[1])
# for row in rows:
#     print(row)
# data_to_insert = {
#     'column1': 'value1',
#     'column2': 'value2',
#     'column3': 'value3'
# }
# dbm.insert_data('my_table', data_to_insert)
# data_to_update = {
#     'column1': 'new_value1',
#     'column2': 'new_value2',
#     'column3': 'new_value3'
# }
# condition = "id = 1"
# dbm.update_data('my_table', data_to_update, condition)