-- Master database script for the chrono sync application
-- DO NOT DELETE 

-- Database Deleting
BEGIN
	USE master 
	IF EXISTS(SELECT name FROM sys.databases WHERE name = 'ChronoSync')
		DROP DATABASE ChronoSync
		PRINT 'ChronoSync Deleted'
END
GO
-- Creating the database
CREATE DATABASE ChronoSync ON PRIMARY(
	NAME = 'ChronoSync_data',
	FILENAME = 'C:\Databases\Database_files\ChronoSync_data.mdf',
	SIZE = 25MB,
	FILEGROWTH = 10%
)
LOG ON(
	NAME = 'ChronoSync_log',
	FILENAME = 'C:\Databases\Log_files\ChronoSync_log.ldf',
	SIZE = 25MB,
	FILEGROWTH = 10%
)
PRINT 'ChronoSync Created'
GO

-- creating the login
BEGIN
	USE ChronoSync
	IF EXISTS(SELECT * FROM sys.syslogins WHERE name = 'api')
		DROP LOGIN api
		PRINT 'api Login DROPPED'
	
	CREATE LOGIN api WITH PASSWORD = 'Qwerty1!'
	PRINT 'api LOGIN CREATED'
END
-- creating the user
 BEGIN
	USE ChronoSync
	IF EXISTS(SELECT * FROM sys.sysusers WHERE name = 'api')
		DROP USER api
		PRINT 'api user DROPPED'
	
	CREATE USER api FOR LOGIN api
	PRINT 'api User CREATED'
END
-- user permissions
BEGIN
	exec sp_addsrvrolemember 'api', 'sysadmin'
	PRINT 'ADDED Sysadmin permissions for api user'
END
-- Creating tables for Chronosync
USE ChronoSync
GO
-- Task Table
CREATE TABLE task(
	t_id INT PRIMARY KEY IDENTITY(1, 1),
	t_name NVARCHAR(100) UNIQUE NOT NULL,
	t_description NVARCHAR(150) NOT NULL
)
PRINT 'CREATED TABLE TASKS'
GO
-- Client Table
CREATE TABLE client(
	c_id INT PRIMARY KEY  IDENTITY(1, 1),
	c_name NVARCHAR(100) NOT NULL,
	c_notes NVARCHAR(MAX) 
)
PRINT 'CREATED TABLE CLIENTS'
GO
-- Employee Table
CREATE TABLE employee(
	e_id INT PRIMARY KEY IDENTITY(1, 1),
	e_name NVARCHAR(50) NOT NULL,
	e_surname NVARCHAR(50) NOT NULL,
	e_email NVARCHAR(50) UNIQUE NOT NULL,
	e_password NVARCHAR(MAX) NOT NULL,
	e_salt NVARCHAR(MAX) NOT NULL,
	e_type NVARCHAR(20) NOT NULL
)
PRINT 'CREATED TABLE EMPLOYEES'
GO
-- Timesheet Table
CREATE TABLE timesheet(
	t_id INT PRIMARY KEY IDENTITY(1, 1),
	t_date DATE NOT NULL,
	t_billable NVARCHAR(1) CHECK(t_billable = 'y' or t_billable = 'n') NOT NULL,
	t_project NVARCHAR(50) NOT NULL,
	t_comment NVARCHAR(MAX) NOT NULL,
	t_start TIME NOT NULL,
	t_end TIME NOT NULL,
	t_spent TIME NOT NULL,
	task_id INT FOREIGN KEY REFERENCES task(t_id) NOT NULL,
	client_id INT FOREIGN KEY REFERENCES client(c_id) NOT NULL
)
PRINT 'CREATED TABLE TIMESHEETS'
GO
-- Bound Table
CREATE TABLE employee_timesheet(
	employee_id INT FOREIGN KEY REFERENCES employee(e_id) NOT NULL,
	timesheet_id INT FOREIGN KEY REFERENCES timesheet(T_id) NOT NULL,
	total_time_worked TIME NOT NULL
)
PRINT 'CREATED TABLE EMPLOYEES TIMESHEET'
GO




select * from employee