import pyodbc
from flask import jsonify

server = 'DESKTOP-VVJU1FS\\SQLEXPRESS'
database = 'csync'
sqlusername = 'chronosyncapi'
sqlpassword = '12345678Q!'
driver = 'ODBC Driver 17 for SQL Server'

con_str = f'''
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    UID={sqlusername};
    PWD={sqlpassword};
    Trusted_Connection=yes;
'''


# login handler
def login(username, password):
    conn = pyodbc.connect(con_str)
    cursor = conn.cursor()
    cursor.execute(f"SELECT employee.id, employee.e_name, employee.e_surname FROM employee WHERE employee.e_email = "
                   f"'{username}' and "
                   f"employee.e_password = '"
                   f"{password}'")
    userdata = cursor.fetchone()
    #u_id = userdata
    print(userdata)
    if userdata is None:
        conn.close()
        return {404: 0}
    else:
        u_info = {200: 1}
        return u_info


# print(login('Jdoe@hotmail.com', 'password'))
# getting user data
def get_sheets(user_id):
    pass
