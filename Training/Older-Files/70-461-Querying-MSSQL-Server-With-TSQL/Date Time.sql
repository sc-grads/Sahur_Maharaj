declare @mydate as datetime = '2015-06-24 12:34:56.124'
SELECT @mydate as mydate

Select DATEFROMPARTS(2015,06,24) AS thisdate
SELECT YEAR(@mydate) as years, MONTH(@mydate), DAY(@mydate) AS datea

SELECT CURRENT_TIMESTAMP as rn
SELECT GETDATE() as datenow
select SYSDATETIME() as datasys

