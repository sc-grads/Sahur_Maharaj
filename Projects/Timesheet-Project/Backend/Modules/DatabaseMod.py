import pyodbc


class Connector:
    def __init__(self):
        self.__server = 'localhost'  # SQL Server hostname or IP address
        self.__database = 'ChronoSync'  # Name of the database
        self.__user = 'api'  # Username for database authentication
        self.__passwd = 'Qwerty1!'  # Password for database authentication
        self.__conn = None  # Connection object

    def connect(self):
        try:
            # Create the connection string using the provided server, database, user, and password
            conn_str = f'DRIVER={{SQL Server}};' \
                       f'SERVER={self.__server};' \
                       f'DATABASE={self.__database};' \
                       f'UID={self.__user};' \
                       f'PWD={self.__passwd}'
            # Establish the database connection
            self.__conn = pyodbc.connect(conn_str)
            # Connection successful
            print(f'Connected to {self.__conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.')
        except pyodbc.Error as e:
            # Connection error occurred
            print(f'Connection error {e}')
        finally:
            # Print a separator line
            print('Connection Open')

    def close(self):
        if self.__conn:
            # Close the database connection if it is open
            self.__conn.close()
            print("Connection closed.")
            print('#' * 50)


        else:
            # Connection was not established
            print('Connection did not close')

    def select(self, table, columns, condition_column=None, condition_value=None, and_condition_column=None,
               and_condition_value=None):
        try:
            cursor = self.__conn.cursor()

            # Build the basic query
            query = f"SELECT {', '.join(columns)} FROM {table}"

            query_values = []

            # Check if there's a condition
            if condition_column is not None and condition_value is not None:
                query += f" WHERE {condition_column} = ?"
                query_values.append(condition_value)

                # Check if there's an additional condition
                if and_condition_column is not None and and_condition_value is not None:
                    query += f" AND {and_condition_column} = ?"
                    query_values.append(and_condition_value)

            cursor.execute(query, query_values)

            rows = cursor.fetchall()

            return rows

        except pyodbc.Error as e:
            return f'Select error: {e}'

    def insert(self, table, columns, values):
        try:
            cursor = self.__conn.cursor()

            # Build the basic query
            query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(values))})"
            cursor.execute(query, values)

            # Commit the transaction
            self.__conn.commit()

            print(f"Successfully inserted data into {table}.")

        except pyodbc.Error as e:
            print(f'Insert error: {e}')
            # Rollback the transaction
            self.__conn.rollback()


if __name__ == '__main__':
    print('Running Module: Database')
    database = Connector()
    database.connect()
    # # Example select
    # database.select('employee', ['e_email', 'e_hashpassword'], 'e_email',
    #                 'sahur.maharaj@sambeconsulting.com', 'e_type', 'SUPERUSER')
    #
    # # Example usage of the insert method
    # table_name = 'employee'
    # columns = ['e_email', 'e_hashpassword', 'e_type']
    # values = ['test@example.com', 'password123', 'USER']
    # database.insert(table_name, columns, values)

    database.close()
