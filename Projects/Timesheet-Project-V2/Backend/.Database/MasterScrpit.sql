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
	e_email NVARCHAR(250) UNIQUE NOT NULL,
	e_hashpassword NVARCHAR(MAX) NOT NULL,
	e_type NVARCHAR(20) CHECK(e_type = 'SUPERUSER' or e_type = 'STANDARD') NOT NULL
)
PRINT 'CREATED TABLE EMPLOYEES'
GO
-- Timesheet Table
CREATE TABLE timesheet(
	t_id INT PRIMARY KEY IDENTITY(1, 1),
	t_date DATE NOT NULL,
	t_billable NVARCHAR(5) CHECK(t_billable = 'True' or t_billable = 'False') NOT NULL,
	t_project NVARCHAR(50) NOT NULL,
	t_comment NVARCHAR(MAX) NOT NULL,
	t_start VARCHAR(5) NOT NULL,
	t_end VARCHAR(5) NOT NULL,
	t_spent NVARCHAR(8) NOT NULL,
	employee_id INT FOREIGN KEY REFERENCES employee(e_id) NOT NULL,
	task_id INT FOREIGN KEY REFERENCES task(t_id) NOT NULL,
	client_id INT FOREIGN KEY REFERENCES client(c_id) NOT NULL
)
PRINT 'CREATED TABLE TIMESHEETS'
GO

-- Inserts

-- employee
INSERT INTO employee
VALUES ('sahur', 'maharaj', 'sahur.maharaj@gmail.com', '8bcsc02aaa6h939u7d0r7c1.890m1cfabb3h21fab2erbfaa7d9jd20S924u36fd8bdh07faf60t4cfae8ae', 'STANDARD'),
		('sahur', 'maharaj', 'sahur.maharaj@sambeconsulting.com', '8bcsc02aaa6h939u7d0r7c1.890m1cfabb3h21fab2erbfaa7d9jd20S924u36fd8bdh07faf60t4cfae8ae', 'SUPERUSER'),  -- password aa
		('John', 'Doe', 'Jdoe@hotmail.com', '59bJ11fdd8eo54de12eS01au2bbd25ch02da633t426a15e83d9fb65da1401e8b49b4e7aeacb', 'STANDARD'), --password Jdoe
		('Jane', 'Doe', 'Jane@gmail.com', 'c9aJd35a876ndd4e401S6deub1fdc1ahc06a062t0e5ab17e3eb0d3b57bd832a7e96c4882080', 'SUPERUSER'); -- Jane01!
-- task 
INSERT INTO task
VALUES
  ('.NET code', 'coding in .NET'),
  ('Admin', 'Admin task'),
  ('Analysis', 'Analysing Tasks'),
  ('Architecture', 'Development'),
  ('Training', 'Udemy courseware'),
  ('Configuration', 'Set up');

-- client
INSERT INTO client
VALUES
  ('Internal', 'SAMBE'),
  ('ABSA', 'A financial services provider'),
  ('ADVTech', 'An IT solutions provider'),
  ('AFA', 'Agricultural and agro-processing company'),
  ('Amplify Health', 'Healthcare technology provider'),
  ('Base 3', 'Provider of business management solutions'),
  ('Dentons', 'International law firm'),
  ('Digiterra', 'A technology and consulting company'),
  ('Standard Bank', 'African financial services company'),
  ('Discovery Bank', 'South African digital bank'),
  ('Discovery Health', 'South African health insurance company'),
  ('Discovery Vitality', 'A wellness and rewards program');

-- timesheet
INSERT INTO timesheet (t_date, t_billable, t_project, t_comment, t_start, t_end, t_spent, employee_id, task_id, client_id)
VALUES
	('2023-04-20', 'True', 'Project A', 'Meeting with client', '09:00', '10:30', '01H30', 1, 1, 1),
	('2023-04-21', 'False', 'Project B', 'Debugging code', '14:00', '16:00', '02H00', 1, 2, 2);

-- selects
select * from task
select * from employee
select * from client
select * from timesheet

SELECT t.t_id, t.t_date, t.t_billable, t.t_project, t.t_comment, t.t_start, t.t_end, t.t_spent, e.e_name, ta.t_name AS task_name, c.c_name AS client_name
FROM timesheet t
JOIN employee e ON t.employee_id = e.e_id
JOIN task ta ON t.task_id = ta.t_id
JOIN client c ON t.client_id = c.c_id ;

