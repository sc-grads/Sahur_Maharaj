CREATE TABLE [dbo].[Employee](
	[EmpID] [int] NOT NULL,
	[EmpName] [nvarchar](50) NULL,
	[EmpTitle] [nvarchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[EmpID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
--------------------------------------------------
CREATE TABLE [dbo].[Sales](
	[EmpID] [int] NULL,
	[EmpName] [nvarchar](50) NULL,
	[SalesNumber] [int] NOT NULL,
	[ItemSold] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[SalesNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
-----------------------------------------------------
SELECT * FROM [dbo].[Employee]
-----------------------------------------------------
SELECT * FROM [dbo].[Sales]

------------------------------------------------------

SELECT * FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpName = s.EmpName
--------------------------------------------------

SELECT * FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
--------------------------------------------------

SELECT e.EmpID,e.EmpName,s.SalesNumber,s.ItemSold FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
order by e.EmpID
-----------------------------------------------

SELECT count(s.SalesNumber),e.EmpID,e.EmpName FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
group by e.EmpID,e.EmpName

----------------------------------------------------------
CREATE TABLE [dbo].[Course](
	[CourseID] [int] NULL,
	[RollNO] [int] NULL
) ON [PRIMARY]

GO

----------------------------------------------------------

CREATE TABLE [dbo].[Student](
	[RollNo] [int] NOT NULL,
	[StudentName] [nvarchar](50) NULL,
	[StudentCity] [nvarchar](20) NULL,
	[StudentPhoneNo] [nvarchar](50) NULL,
	[StuentAge] [int] NULL,
 CONSTRAINT [PK_Student] PRIMARY KEY CLUSTERED 
(
	[RollNo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
--------------------------------------------------------
select * from [dbo].[Student]
-----------------------------------------------------
select * from [dbo].[Course]
 ------------------------------------------------

select * from [dbo].[Student] s
inner join [dbo].[Course] c 
on s.RollNo = c.RollNO


-------------------------------------------

select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
inner join [dbo].[Course] c 
on s.RollNo = c.RollNO

----------------------------------------------------

select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
join [dbo].[Course] c 
on s.RollNo = c.RollNO

-----------------------------------------------------------

select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
left join [dbo].[Course] c 
on s.RollNo = c.RollNO

-------------------------------------------------------------

select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
right join [dbo].[Course] c 
on s.RollNo = c.RollNO

----------------------------------------------------

select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
full join [dbo].[Course] c 
on s.RollNo = c.RollNO