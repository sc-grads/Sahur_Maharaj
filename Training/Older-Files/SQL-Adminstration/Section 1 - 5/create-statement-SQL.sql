CREATE DATABASE [FirstDatabase]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'FirstDatabase', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\FirstDatabase_data' , SIZE = 20480KB , MAXSIZE = 10240KB , FILEGROWTH = 10%)
 LOG ON 
( NAME = N'FirstDatabase_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\FirstDatabase_log' , SIZE = 8192KB , MAXSIZE = 10240KB , FILEGROWTH = 10%)
GO

USE [FirstDatabase]
GO
USE [FirstDatabase]
GO
IF NOT EXISTS (SELECT name FROM sys.filegroups WHERE is_default=1 AND name = N'PRIMARY') ALTER DATABASE [FirstDatabase] MODIFY FILEGROUP [PRIMARY] DEFAULT
GO
USE [FirstDatabase]
GO

/****** Object:  Table [dbo].[Personal_info]    Script Date: 2023/02/27 13:06:03 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Personal_info](
	[id] [int] NOT NULL,
	[firstname] [varchar](50) NULL,
	[dob] [datetime] NULL,
 CONSTRAINT [PK_Personal_info] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


