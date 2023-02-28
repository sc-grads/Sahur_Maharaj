CREATE TABLE [dbo].[salesstaff](
	[staffid] [int] NOT NULL PRIMARY KEY,
	[fName] [nvarchar](30) NULL,
	[lName] [nvarchar](30) NULL,
	)
GO
-- DROP TABLE dbo.salesstaff
-- DROP TABLE dbo.salesstaffNew
 -- DROP TABLE dbo.nameonlytable
 -- DROP TABLE dbo.salesstaffNew_bkp

-----------------------------------------------

INSERT INTO [dbo].[salesstaff] (STAFFID,FNAME,LNAME) VALUES (200,'Abbas','Mehmood')

------------------------------------------------------

INSERT INTO [dbo].[salesstaff] (STAFFID,FNAME,LNAME) VALUES (300,'Imran','Afzal'),(325,'John','Vick'),(314,'James','Dino')

-----------------------------------------------------

CREATE TABLE [dbo].[salesstaffNew](
	ID [int] not null IDENTITY PRIMARY KEY,
	[staffid] [int] NOT NULL,
	[fName] [nvarchar](30),
	[lName] [nvarchar](30)
	)
GO

---------------------------------------------------------

SELECT * FROM salesstaffNew

----------------------

INSERT INTO [dbo].[salesstaffNew] (STAFFID,FNAME,LNAME) VALUES (200,'Abbas','Mehmood')

--------------------------------------

INSERT INTO [dbo].[salesstaffNew] (STAFFID,FNAME,LNAME) VALUES (300,'Imran','Afzal'),(325,'John','Vick'),(314,'James','Dino')

-----------------------------------
CREATE TABLE [dbo].[nameOnlyTable](
	
	[fName] [nvarchar](30),
	[lName] [nvarchar](30)
	)

GO
------------------------------------
select * from [nameOnlyTable]

-------------------------------------

insert into nameOnlyTable (fname,lname)
select fname,lname from salesstaffNew where id >= 3

--------------------------------

select * into salesstaffNew_bkp from salesstaffNew

-----------------------------------