import pyodbc

server = 'DESKTOP-VVJU1FS\\SQLEXPRESS'
database = 'ecommerceDB'
username = 'EcommerceAdmin'
password = '12345678Q!'
driver = 'ODBC Driver 17 for SQL Server'

con_str =f'''
	DRIVER={driver};
	SERVER={server};
	DATABASE={database};
	UID={username};
	PWD={password};
	Trusted_Connection=yes;
''' 

conn = pyodbc.connect(con_str)
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE u_name = 'Harry'")
u_name = cursor.fetchall()
print(u_name[0][1][::-1])
# for row in cursor.fetchall():
#     print(row)

conn.close()


def test():
    print(f'Hello {database}')


test()
