USE csync
GO
-- Creating login for application
BEGIN
IF EXISTS(SELECT * FROM sys.syslogins WHERE NAME = 'chronosyncapi')
	DROP LOGIN chronosyncapi -- Deleting login
	PRINT 'DROPPED LOGIN chronosyncapi'
END
CREATE LOGIN chronosyncapi WITH PASSWORD = '12345678Q!'
PRINT 'LOGIN CREATED FOR CHRONOSYNCAPI'
GO
-- Creating user for application
BEGIN
IF EXISTS(SELECT * FROM sys.sysusers WHERE NAME = 'chronosyncapi')
	DROP USER chronosyncapi -- Deleting user
	PRINT 'DROPPPED USER CHRONOSYNCAPI'
END
CREATE USER chronosyncapi FOR LOGIN chronosyncapi
PRINT 'CREATED USER CHRONOSYNCAPI'
GO
-- User Permissions
-- EXEC sp_addsrvrolemember 'csyncapi', 'public'
-- Deleting and recreating the database
BEGIN
USE master
	IF EXISTS(SELECT NAME FROM sys.databases WHERE NAME = 'csync')
		DROP DATABASE csync
		PRINT 'DROPPED DATABASE CSYNC'
END
GO
-- Creating application database
CREATE DATABASE csync ON PRIMARY(
	NAME = 'csync_data',
	FILENAME = 'C:\DATABASE\DATABASE_FILES\csync_data.mdf',
	SIZE = 20MB,
	FILEGROWTH = 10%
)
LOG ON(
	NAME = 'csync_log',
	FILENAME = 'C:\DATABASE\DATABASE_LOGS\csync_data.ldf',
	SIZE = 20MB,
	FILEGROWTH = 10%
)
PRINT 'CREATED DATABASE CSYNC'
GO

-- Creating tables in the database
USE csync
GO
-- task table
CREATE TABLE task(
	id INT PRIMARY KEY IDENTITY(1, 1),
	t_name VARCHAR(50) NOT NULL,
	t_description VARCHAR(200) NOT NULL
)
PRINT 'CREATED TABLE TASK'
GO
-- client table
CREATE TABLE client(
	id INT PRIMARY KEY IDENTITY(1, 1),
	c_name VARCHAR(50) NOT NULL,
	c_address VARCHAR(100) NOT NULL,
	c_notes TEXT
)
PRINT 'CREATED TABLE CLIENT'
GO
-- employee table
CREATE TABLE employee(
	id INT PRIMARY KEY IDENTITY (1, 1),
	e_name VARCHAR(50) NOT NULL,
	e_surname VARCHAR(50) NOT NULL,
	e_email VARCHAR(50) UNIQUE NOT NULL,
	e_password VARCHAR(100) NOT NULL
)
PRINT 'CREATED TABLE EMPLOYEE'
GO
-- timesheet table
CREATE TABLE timesheet(
	id INT PRIMARY KEY IDENTITY(1, 1),
	t_Date DATE NOT NULL,
	t_Project VARCHAR(50),
	t_Billable VARCHAR(1) NOT NULL,
	t_Notes TEXT NOT NULL,
	t_TimeIn TIME NOT NULL,
	t_TimeOut TIME NOT NULL,
	t_TimeSpent TIME NOT NULL,
	t_id INT FOREIGN KEY REFERENCES task(id) NOT NULL,
	c_id INT FOREIGN KEY REFERENCES client(id) NOT NULL
)
PRINT 'CREATED TABLE TIMESHEET'
GO
-- employee / timesheet
CREATE TABLE e_ts(
	e_id INT FOREIGN KEY REFERENCES employee(id) NOT NULL,
	t_id INT FOREIGN KEY REFERENCES timesheet(id) NOT NULL,
	total_time TIME NOT NULL
)
PRINT 'CREATED BOUND TABLE'
GO

-- Adding demo data into database
-- Adding demo data into employee
INSERT INTO employee(e_name, e_surname, e_email, e_password) VALUES
	('John', 'Doe', 'Jdoe@hotmail.com', 'Apassword'),
	('Jane', 'Doe', 'Jdoe2@gmail.com', 'AnotherPassword'),
	('Shudi', 'Maha', 'shuMaha@gmail.com', 'Supersecretpassword'),
	('Shay', 'Maha', 'shamaha@yahoo.com', 'onemorepassword')
PRINT 'ADDED DEMO EMPLOYEE DATA'
GO
-- Adding demo data into task
INSERT INTO task VALUES
	('Training','Learning matirial'),
	('Configuaration','Setting up system'),
	('Design','Creating diagrams'),
	('Udemy','Compleating/starting a course')
PRINT 'ADDED DEMO TASK DATA'
GO
-- Adding demo data into client
INSERT INTO client VALUES
	('Internal', 'home', 'internal company jobs'),
	('client 1', 'away', 'new client'),
	('client 2', 'away', 'existing client'),
	('client 3', 'away', 'good realationship')
PRINT 'ADDED DEMO CLIENT DATA'
GO

-- Adding demo data into timesheet
INSERT INTO timesheet(t_Date, t_Project, t_Billable, t_Notes, t_TimeIn, t_TimeOut, t_TimeSpent, t_id, c_id) VALUES 
	('2023-01-22', 'Project 1', 'N', 'client worked away', '08:00', '14:00', '06:00', 1, 3),
	('2023-01-22', 'Project 1', 'N', 'client worked away', '14:00', '17:00', '03:00', 1, 3),
	('2023-03-23', 'Project 3', 'Y', 'None', '18:00', '13:00', '05:00', 2, 2),
	('2023-11-22', 'Project 1', 'N', 'Udemy Course', '14:00', '17:00', '03:00', 4, 4)
PRINT 'ADDED DEMO TIMESHEET DATA'
GO
-- Adding demo data into e_ts
INSERT INTO e_ts(e_id, t_id, total_time) VALUES
	(1, 1, '09:00'),
	(1, 2, '09:00'),
	(2, 3, '05:00'),
	(4, 4, '03:00')
PRINT 'ADDED DEMO EMPLOYEE / TIMESHEET DATA'
GO
-- Triggers

-- Indexes

-- Procedures

-- Selects
SELECT * FROM e_ts
SELECT * FROM task
SELECT * FROM timesheet
SELECT * FROM employee
SELECT * FROM client

SELECT @@SERVERNAME
SELECT DB_NAME()