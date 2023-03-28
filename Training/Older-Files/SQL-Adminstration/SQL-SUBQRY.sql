/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [BusinessEntityID]
      ,[RateChangeDate]
      ,[Rate]
      ,[PayFrequency]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[HumanResources].[EmployeePayHistory]

 ------------------------------------------------------------------------------


  select * from [Production].[Product]

-------------------------------------------------------------------------------------

  select * from [Production].[ProductInventory]

-- ALL TABLES GET CREATED IN DBO SCHEMA UNLESS WE CREATE A NEW SCHEMA

-------------------------------------------------------------------------------------


SELECT * FROM dbo.EMPLOYEE

-----------------------------------

SELECT *
  FROM [HumanResources].[EmployeePayHistory]
  WHERE [BusinessEntityID] IN (SELECT BusinessEntityID FROM [HumanResources].[EmployeePayHistory] WHERE Rate > 60)

----------------------------------------

SELECT *
  FROM [HumanResources].[EmployeePayHistory]
  WHERE [BusinessEntityID] IN (SELECT BusinessEntityID FROM [HumanResources].[EmployeePayHistory] WHERE Rate = 39.06)

---------------------------------------------

 select * from [Production].[Product]
 where ProductID in ( select ProductID from [Production].[ProductInventory] where Quantity > 300)
