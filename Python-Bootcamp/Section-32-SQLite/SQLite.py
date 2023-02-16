# Serverless db no config
import sqlite3
connection = sqlite3.connect('store_data.db')

cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER,
        name VARCHAR(25),
        department VARCHAR(30),
        cell VARCHAR(10),
        email VARCHAR(100)
    )
"""

cursor.execute(sql)
cursor.close()
connection.commit()
connection.close()

# CRUD OPS
# insert
connection = sqlite3.connect('store_data.db')

cursor_1 = connection.cursor()
sql_ins = """
    INSERT INTO employees (id, name, department, cell, email) VALUES (1, "John Smith", "IT", "+123456789", "johns@mycompany.com");
    INSERT INTO employees VALUES (2, "Anne Barker", "Accounting", "+155345789", "anne@mycompany.com");
    INSERT INTO employees VALUES (3, "Antony Winter", "Sales", "0042345678911", "danw@mycompany.com");
"""

cursor_1.executescript(sql_ins)
cursor_1.close()
connection.close()

# Select
connection = sqlite3.connect('store_data.db')
cursor_2 = connection.cursor()
sql = 'select * from employees'
# sql = 'select * from employees where name LIKE "A%" order by name desc'
cursor_2.execute(sql)

for row in cursor_2.fetchall():
    print(row)

connection.commit()
connection.close()

# params
connection = sqlite3.connect('store_data.db')
cursor_3 = connection.cursor()
id = input('Enter ID:')

# ? is placeholder, will be replaced with id entered by the user
sql = 'select * from employees where id = ?;'

cursor_3.execute(sql, (id,))

for row in cursor_3.fetchall():
    print(row)

record = (10, 'Leonardo Romano', 'Marketing', '+40122111', 'leo@x.com')
sql = 'insert into employees values (?,?,?,?,?);'
cursor_3.execute(sql, record)

connection.commit()
connection.close()

# updates
connection = sqlite3.connect('store_data.db')

cursor_4 = connection.cursor()
id = input('Id:')

sql = 'UPDATE employees SET department="Sales" where id=?;'
cursor_4.execute(sql, (id,))
connection.commit()
connection.close()

# Removing
connection = sqlite3.connect('store_data.db')

cursor_6 = connection.cursor()

department = input('Department:')

sql = 'DELETE FROM employees where department = ?;'
cursor_6.execute(sql, (department,))

connection.commit()
connection.close()

