-- Database user creation for admin
-- remove existing user
IF EXISTS(SELECT * FROM sys.syslogins WHERE NAME = 'EcommerceAdmin')
	DROP LOGIN EcommerceAdmin
	PRINT 'DROPPED LOGIN FOR USER: EcommerceAdmin'
GO
-- remove user for client
IF EXISTS(SELECT * FROM sys.sysusers WHERE NAME = 'EcommerceAdmin')
	DROP USER EcommerceAdmin
	PRINT 'DROPPED USER FOR USER: EcommerceAdmin'
GO
-- recreating the user
CREATE LOGIN EcommerceAdmin WITH PASSWORD = '12345678Q!'
CREATE USER EcommerceAdmin FOR LOGIN EcommerceAdmin
PRINT 'CREATED USER AND LOGIN FOR USER: EcommerceAdmin'
GO
-- adding permissions for admin
EXEC sp_addsrvrolemember 'EcommerceAdmin', 'sysadmin'
PRINT 'PERMISSION sysadmin GIVEN TO USER: EcommerceAdmin'
GO


-- Creating the database
CREATE DATABASE ecommerceDB ON PRIMARY(
	NAME = 'wcommerceDB_data',
	FILENAME = 'C:\Databases\ecommerceDB_datat.mdf',
	SIZE = 2MB,
	FILEGROWTH = 10%
)
LOG ON(
	NAME = 'ecommerceDB_log',
	FILENAME = 'C:\Databases\ecommerceDB_datat.ldf',
	SIZE = 2MB,
	FILEGROWTH = 10%
)
GO

-- Creating the tables
USE ecommerceDB
GO
CREATE TABLE users(
	u_id INT PRIMARY KEY IDENTITY(1, 1),
	u_name VARCHAR(50) NOT NULL,
	u_passwd VARCHAR(50) NOT NULL,
	u_email VARCHAR(30) NOT NULL
)

-- Inserting demo data

INSERT INTO users VALUES('Shay', '*****', 'Shaay@ee.com'), ('Harry','****','Harry@ee.com')
SELECT * FROM users