CREATE TABLE SQLBackupRestoreTest (
	ID INT NOT NULL PRIMARY KEY,
	loginname VARCHAR(100) NOT NULL,
	logindate DATETIME NOT NULL DEFAULT getdate()
)
GO


select *  from SQLBackupRestoreTest
-- 21 rows
insert into SQLBackupRestoreTest (ID,loginname) values (1, 'test1')
insert into SQLBackupRestoreTest (ID,loginname) values (2, 'test2')
insert into SQLBackupRestoreTest (ID,loginname) values (3, 'test3')
insert into SQLBackupRestoreTest (ID,loginname) values (4, 'test4')
insert into SQLBackupRestoreTest (ID,loginname) values (5, 'test5')

-- FULL Back up 5 rows

insert into SQLBackupRestoreTest (ID,loginname) values (6, 'test6')
insert into SQLBackupRestoreTest (ID,loginname) values (7, 'test7')
insert into SQLBackupRestoreTest (ID,loginname) values (8, 'test8')
insert into SQLBackupRestoreTest (ID,loginname) values (9, 'test9')
insert into SQLBackupRestoreTest (ID,loginname) values (10, 'test10')

-- diff backup up 10 rows

insert into SQLBackupRestoreTest (ID,loginname) values (11, 'test11')
insert into SQLBackupRestoreTest (ID,loginname) values (12, 'test12')
insert into SQLBackupRestoreTest (ID,loginname) values (13, 'test13')

-- tran log back - 1 up 13 rows

insert into SQLBackupRestoreTest (ID,loginname) values (14, 'test14')
insert into SQLBackupRestoreTest (ID,loginname) values (15, 'test15')
insert into SQLBackupRestoreTest (ID,loginname) values (16, 'test16')
insert into SQLBackupRestoreTest (ID,loginname) values (17, 'test17')


--FULL and DIFF

-- tran log back - 2 up 17 rows
-- Jul 26 2021  8:48AM
insert into SQLBackupRestoreTest (ID,loginname) values (114, 'test14')


-- Jul 26 2021  8:49AM
insert into SQLBackupRestoreTest (ID,loginname) values (115, 'test15')
-- Jul 26 2021  8:40AM
--- Transaction Log 
--Jul 26 2021  8:42AM


--Jul 26 2021  8:53AM

insert into SQLBackupRestoreTest (ID,loginname) values (116, 'test16')
insert into SQLBackupRestoreTest (ID,loginname) values (117, 'test17')
-- Jul 26 2021  8:42AM

-- 
--

print getdate()
-- Jul 26 2021  7:17AM

USE [master]
RESTORE DATABASE [AdventureWorks2019] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2019_full.BAK' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5

GO

USE [master]
RESTORE DATABASE [AdventureWorks2019] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2019_diff_1.diff' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5

GO

RESTORE LOG [AdventureWorks2019] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2019_tran_3.trn' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 10
GO


RESTORE DATABASE [AdventureWorks2019_RestoreTest] WITH RECOVERY
GO


USE [master]
RESTORE DATABASE [AdventureWorks2019_RestoreTest] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2019_full.BAK' WITH  FILE = 3,  
MOVE N'AdventureWorks2019_Data' TO N'C:\SQL_DATA_FILES\AdventureWorks2019_RestoreTest_Data.mdf',  MOVE N'AdventureWorks2019_Log' 
TO N'C:\SQL_LOG_FILES\AdventureWorks2019_RestoreTest_Log.ldf',  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE DATABASE [AdventureWorks2019_RestoreTest] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2019_diff_1.diff' WITH  FILE = 3,  NORECOVERY,  NOUNLOAD,  STATS = 5

GO


RESTORE LOG [AdventureWorks2019_RestoreTest] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2019_tran_final.trn' WITH  FILE = 1,  NOUNLOAD,  STATS = 10, 
 STOPAT = N'2021-07-26T08:54:23'
GO
