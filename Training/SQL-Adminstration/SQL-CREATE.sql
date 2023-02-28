
-- First Create [sales].[storesnew]
create table [AdventureWorks2019].[sales].[storesnew] (
store_id INT  PRIMARY KEY not null,
sales INT
)

-- Then create the [sales].[visists] with foreign key
create table [AdventureWorks2019].[sales].[visists] (
visit_ID INT PRIMARY KEY identity (1,1),
first_name VARCHAR (50) not null,
last_name VARCHAR (50) not null,
visited_at datetime,
phone VARCHAR (20) not null,
store_id INT not null,
foreign key (store_id) References sales.storesnew (store_id)	
)

select * from [person].[person]

select [BusinessEntityID],[FirstName],[MiddleName],[Title]
 from [person].[person]

 -- SELECT INTO TEMPTABLE
 select [BusinessEntityID],[FirstName],[MiddleName],[Title]
 into #TempPersonTable
 from [person].[person]

 select * from #TempPersonTable


-- DROP TEMP TABLE IF YOU ARE USING THE SAME SESSION
Drop table #TempPersonTable

 -- CREATE TEMPTABLE AND POPULATE IT
 create table #TempPersonTable (
 BusinessEntityID INT,
 FirstName NVARCHAR(50),
 MiddleName NVARCHAR(50),
 Title NVARCHAR(50)
 )

 -- minsert into for temp table

 Insert into #TempPersonTable
select [BusinessEntityID],[FirstName],[MiddleName],[Title]
 from [person].[person]