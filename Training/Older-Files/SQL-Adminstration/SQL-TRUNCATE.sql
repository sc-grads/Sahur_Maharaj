select * from salesstaff

-------------------------

truncate  table salesstaff

-----------------------------

create table employeenew (
id int identity (1,1) not null,
employeename nvarchar(50) not null
)

----------------------

insert into employeenew
(employeename)
values ('Abbas'),('Imran'),('dino'),('james')

--------------------

delete from employeenew

--------------------

truncate table  employeenew