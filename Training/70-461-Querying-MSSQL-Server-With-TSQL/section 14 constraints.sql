select * from tblEmployee where EmployeeNumber = 2001

select T.EmployeeNumber as TEmployeeNumber,
       E.EmployeeNumber as EEmployeeNumber,
	   sum(Amount) as SumAmount
from tblTransaction AS T
LEFT JOIN tblEmployee AS E
ON T.EmployeeNumber = E.EmployeeNumber
group by T.EmployeeNumber, E.EmployeeNumber
order by EEmployeeNumber

BEGIN TRAN
UPDATE tblEmployee
SET DateOfBirth = '2101-01-01'
WHERE EmployeeNumber = 537
select * from tblEmployee ORDER BY DateOfBirth DESC
ROLLBACK TRAN

BEGIN TRAN
UPDATE tblEmployee
SET EmployeeGovernmentID = 'aaaa'
WHERE EmployeeNumber BETWEEN 530 AND 539
select * from tblEmployee ORDER BY EmployeeGovernmentID ASC
ROLLBACK TRAN

insert into tblEmployee
select NULL, EmployeeFirstName, EmployeeMiddleName, EmployeeLastName, EmployeeGovernmentID, DateOfBirth, Department
from tblEmployee

INSERT INTO tblEmployee
values (2001, 'FirstName', 'M', 'LastName', 'AB123456C', '1994-01-01', 'Commerical')
INSERT INTO tblEmployee
values (null, 'AnotherFirstName', 'N', 'AnotherLastName', 'AB123457C', '1994-01-02', 'Finance')

delete from tblEmployee
Where EmployeeNumber > 2000

alter table tblEmployee
ADD CONSTRAINT unqGovernmentID UNIQUE (EmployeeGovernmentID);

select EmployeeGovernmentID, count(EmployeeGovernmentID) as MyCount from tblEmployee
group by EmployeeGovernmentID
having count(EmployeeGovernmentID)>1

select * from tblEmployee where EmployeeGovernmentID IN ('HN513777D', 'TX593671R')

begin tran
delete from tblEmployee
where EmployeeNumber < 3

delete top(2) from tblEmployee
where EmployeeNumber in (131, 132)

select * from tblEmployee where EmployeeGovernmentID IN ('HN513777D', 'TX593671R')

commit tran

alter table tblTransaction
add constraint unqTransaction UNIQUE (Amount, DateOfTransaction, EmployeeNumber)

delete from tblTransaction
where EmployeeNumber = 131

insert into tblTransaction
VALUES (1,'2015-01-01', 131)
insert into tblTransaction
VALUES (1,'2015-01-01', 131)

alter table tblTransaction
Drop constraint unqTransaction

create table tblTransaction2
(Amount smallmoney not null,
DateOfTransaction smalldatetime not null,
EmployeeNumber int not null,
CONSTRAINT unqTransaction2 UNIQUE (Amount,DateOfTransaction,EmployeeNumber))

drop table tblTransaction2


alter table tblTransaction
add DateOfEntry datetime

alter table tblTransaction
add constraint defDateOfEntry DEFAULT GETDATE() for DateOfEntry;

delete from tblTransaction where EmployeeNumber < 3

insert into tblTransaction(Amount, DateOfTransaction, EmployeeNumber)
values (1, '2014-01-01', 1)
insert into tblTransaction(Amount, DateOfTransaction, EmployeeNumber, DateOfEntry)
values (2, '2014-01-02', 1, '2013-01-01')

select * from tblTransaction where EmployeeNumber < 3

create table tblTransaction2
(Amount smallmoney not null,
DateOfTransaction smalldatetime not null,
EmployeeNumber int not null,
DateOfEntry datetime null CONSTRAINT tblTransaction2_defDateOfEntry DEFAULT GETDATE())

insert into tblTransaction2(Amount, DateOfTransaction, EmployeeNumber)
values (1, '2014-01-01', 1)
insert into tblTransaction2(Amount, DateOfTransaction, EmployeeNumber, DateOfEntry)
values (2, '2014-01-02', 1, '2013-01-01')

select * from tblTransaction2 where EmployeeNumber < 3

drop table tblTransaction2

alter table tblTransaction
drop column DateOfEntry

alter table tblTransaction
drop constraint defDateOfEntry

BEGIN TRAN

ALTER TABLE tblTransaction
ADD DateOfEntry datetime
DEFAULT GETDATE() WITH VALUES

SELECT * FROM tblTransaction

ROLLBACK TRAN
