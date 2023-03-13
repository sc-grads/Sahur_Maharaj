USE [70-461]
GO
CREATE TABLE tblEmployee(
	EmployeeNumber INT,
	EmployeeName VARCHAR(50),
)

DECLARE @myVar AS INT = 2
SELECT @myVar AS Variables

SET @myVar = 22
SELECT @myVar AS modded

SET @myVar = @myVar * 4
SELECT @myVar AS Multi



