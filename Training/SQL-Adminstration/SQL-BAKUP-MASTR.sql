
-- CREATE TEST USER


BACKUP DATABASE [master] TO  DISK = N'C:\SQL_BACKUPS\master_backup.bak' WITH NOFORMAT, NOINIT,  NAME = N'master-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO

restore database master from disk = 'C:\SQL_BACKUPS\master_backup.bak' with replace;

-- RUN CMS as Admin and Type
net stop mssqlserver


net start mssqlserver /m

restore database master_recovery from disk = 'C:\SQL_BACKUPS\master_backup_testrestore.bak' with
move 'master' to 'C:\master_recovery.mdf',
move 'mastlog' to 'C:\mastlog_recovery.ldf';

-- C:\SQL_DATA_FILES\MSSQL13.MSSQLSERVER\MSSQL\DATA


USE [master]
GO
EXEC master.dbo.sp_detach_db @dbname = N'master_recovery'
GO