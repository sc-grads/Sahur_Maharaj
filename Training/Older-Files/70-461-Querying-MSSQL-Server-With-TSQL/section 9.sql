-- Creation of tblEmployee table
CREATE TABLE tblEmployee
(
EmployeeNumber INT NOT NULL,
EmployeeFirstName VARCHAR(50) NOT NULL,
EmployeeMiddleName VARCHAR(50) NULL,
EmployeeLastName VARCHAR(50) NOT NULL,
EmployeeGovernmentID CHAR(10) NULL,
DateOfBirth DATE NOT NULL
)
--Adding additional columns
ALTER TABLE tblEmployee
ADD Department VARCHAR(10);

SELECT * FROM tblEmployee

INSERT INTO tblEmployee
VALUES (132, 'Dylan', 'A', 'Word', 'HN513777D', '19920914', 'Customer Relations')

ALTER TABLE tblEmployee
DROP COLUMN Department

ALTER TABLE tblEmployee
ADD Department VARCHAR(15)

ALTER TABLE tblEmployee
ALTER COLUMN Department VARCHAR(20)

ALTER TABLE tblEmployee
ALTER COLUMN Department VARCHAR(19)

SELECT LEN( 'Customer Relations')

INSERT INTO tblEmployee([EmployeeFirstName],[EmployeeMiddleName],
[EmployeeLastName],[EmployeeGovernmentID],[DateOfBirth],[Department],[EmployeeNumber])
VALUES ('Jossef', 'H', 'Wright', 'TX593671R', '19711224', 'Litigation',131)

INSERT INTO tblEmployee
VALUES (1, 'Dylan', 'A', 'Word', 'HN513777D', '19920914', 'Customer Relations'),
(2,'Jossef', 'H', 'Wright', 'TX593671R', '19711224', 'Litigation')
--WHERE and LIKE

select * from tblEmployee
where [EmployeeLastName] <> 'Word'

select * from tblEmployee
where [EmployeeLastName] like '_W%'

Select * from tblEmployee
where [EmployeeLastName] like '[r-t]%'

Select * from tblEmployee
where [EmployeeLastName] like '[^rst]%'

-- % = 0-infinity characters
-- _ = 1 character
-- [A-G] = In the range A-G.
-- [AGQ] = A, G or Q.
-- [^AGQ] = NOT A, G or Q.

select * from tblEmployee
where EmployeeLastName like '[%]%'

select * from tblEmployee
where EmployeeLastName like '`%%' ESCAPE '`'
--SELECTing only part of a table – numbers
select * from tblEmployee
where not EmployeeNumber>200

select * from tblEmployee
where EmployeeNumber!=200

select * from tblEmployee
where EmployeeNumber>=200 and EmployeeNumber<=209

select * from tblEmployee
where not (EmployeeNumber>=200 and EmployeeNumber<=209)

select * from tblEmployee
where EmployeeNumber<200 or EmployeeNumber>209

select * from tblEmployee
where EmployeeNumber between 200 and 209

select * from tblEmployee
where EmployeeNumber not between 200 and 209

select * from tblEmployee
where EmployeeNumber in (200, 204, 208)
--Summarising an ordering data
select * from tblEmployee
where DateOfBirth between '19760101' and '19861231'

select * from tblEmployee
where DateOfBirth >= '19760101' and DateOfBirth < '19870101'

select * from tblEmployee
where year(DateOfBirth) between 1976 and 1986  -- DO NOT USE.

SELECT year(DateOfBirth) as YearOfDateOfBirth, count(*) as NumberBorn
FROM tblEmployee
GROUP BY year(DateOfBirth)

SELECT * FROM tblEmployee
where year(DateOfBirth) = 1967

SELECT year(DateOfBirth) as YearOfDateOfBirth, count(*) as NumberBorn
FROM tblEmployee
WHERE 1=1
GROUP BY year(DateOfBirth)
-- non-deterministic

SELECT year(DateOfBirth) as YearOfDateOfBirth, count(*) as NumberBorn
FROM tblEmployee
WHERE 1=1
GROUP BY year(DateOfBirth)
ORDER BY year(DateOfBirth) DESC
-- deterministic
--Criteria on summarised data
select left(EmployeeLastName,1) as Initial, count(*) as CountOfInitial
from tblEmployee
group by left(EmployeeLastName,1)
order by count(*) DESC --left(EmployeeLastName,1)

select top(5) left(EmployeeLastName,1) as Initial, count(*) as CountOfInitial
from tblEmployee
group by left(EmployeeLastName,1)
order by count(*) DESC --left(EmployeeLastName,1)

select left(EmployeeLastName,1) as Initial, count(*) as CountOfInitial
from tblEmployee
where DateOfBirth > '19860101'
group by left(EmployeeLastName,1)
having count(*)>=20
order by CountOfInitial DESC 

Update tblEmployee
Set EmployeeMiddleName = NULL
Where EmployeeMiddleName = ''
--Exercise
select COUNT(EmployeeMiddleName) as NumberOfMiddleNames,
count(*)-count(EmployeeMiddleName) as NoMiddleName,
format(min(DateOfBirth),'dd-MM-yy') as EarliestDateOfBirth,
format(max(DateOfBirth),'D') as LatestDateOfBirth
FROM tblEmployee
GROUP BY DATENAME(MONTH,DateOfBirth), DATEPART(MONTH,DateOfBirth)
ORDER BY DATEPART(MONTH,DateOfBirth)
--Different Types of JOIN

select tblEmployee.EmployeeNumber, EmployeeFirstName, EmployeeLastName, sum(Amount) as SumOfAmount
from tblEmployee left join tblTransaction
on tblEmployee.EmployeeNumber = tblTransaction.EmployeeNumber
GROUP BY tblEmployee.EmployeeNumber, EmployeeFirstName, EmployeeLastName
ORDER BY EmployeeNumber

select * from tblEmployee 

select * from tblTransaction where EmployeeNumber = 1046
--Creating a third table
select Department as NumberOfDepartments
into tblDepartment2
from
(select Department, count(*) as NumberPerDepartment
from tblEmployee
GROUP BY Department) as newTable

--derived table

select distinct Department, convert(varchar(20), N'') as DepartmentHead
into tblDepartment
from tblEmployee

drop table tblDepartment

select * from tblDepartment

alter table tblDepartment
alter column DepartmentHead varchar(30) null
--JOINING three tables
select DepartmentHead, sum(Amount) as SumOfAmount
from tblDepartment
left join tblEmployee
on tblDepartment.Department = tblEmployee.Department
left join tblTransaction
on tblEmployee.EmployeeNumber = tblTransaction.EmployeeNumber
group by DepartmentHead
order by DepartmentHead

insert into tblDepartment(Department,DepartmentHead)
values ('Accounts', 'James')

select D.DepartmentHead, Sum(T.Amount) as SumOfAmount
from tblDepartment as D
left join tblEmployee as E
on D.Department = E.Department
left join tblTransaction T
on E.EmployeeNumber = T.EmployeeNumber
group by D.DepartmentHead
order by D.DepartmentHead

--Missing data
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
left join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
where T.EmployeeNumber IS NULL
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName
order by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName
-- derived table

select ENumber, EmployeeFirstName, EmployeeLastName
from (
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
left join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName) as newTable
where TNumber is null
order by ENumber, TNumber, EmployeeFirstName,
       EmployeeLastName
-- RIGHT JOIN

select *
from (
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName) as newTable
where ENumber is null
order by ENumber, TNumber, EmployeeFirstName,
       EmployeeLastName
--Deleting data
-- Version 1

begin transaction

select count(*) from tblTransaction

delete tblTransaction
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber is null

select count(*) from tblTransaction

rollback transaction

select count(*) from tblTransaction
-- Version 2

begin transaction
select count(*) from tblTransaction

delete tblTransaction
from tblTransaction
where EmployeeNumber IN
(select TNumber
from (
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName) as newTable
where ENumber is null)
select count(*) from tblTransaction
rollback tran
select count(*) from tblTransaction
--Updating data
select * from tblEmployee where EmployeeNumber = 194
select * from tblTransaction where EmployeeNumber = 3
select * from tblTransaction where EmployeeNumber = 194

begin tran
-- select * from tblTransaction where EmployeeNumber = 194

update tblTransaction
set EmployeeNumber = 194
output inserted.EmployeeNumber, deleted.EmployeeNumber
from tblTransaction
where EmployeeNumber in (3, 5, 7, 9)

insert into tblTransaction
go
delete tblTransaction
from tblTransaction
where EmployeeNumber = 3

-- select * from tblTransaction where EmployeeNumber = 194
rollback tran


