select * from tblEmployee where EmployeeMiddleName is null

declare @myOption as varchar(10) = 'Option B'
select isnull(@myOption, 'No Option') as MyOptions
go

declare @myFirstOption as varchar(10) --= 'Option A'
declare @mySecondOption as varchar(10) --= 'Option B'

select coalesce(@myFirstOption, @mySecondOption, 'No option') as MyOptions
go

select isnull('ABC',1) as MyAnswer
select coalesce('ABC',1) as MyOtherAnswer
go

select isnull(null,null) as MyAnswer
select coalesce(null,null) as MyOtherAnswer
go

create table tblExample
(myOption nvarchar(10) null)
go
insert into tblExample (myOption)
values ('Option A')

select coalesce(myOption, 'No option') as MyOptions
into tblIsCoalesce
from tblExample 
select case when myOption is not null then myOption else 'No option' end as myOptions from tblExample
go
select isnull(myOption, 'No option') as MyOptions
into tblIsNull
from tblExample 
go

drop table tblExample
drop table tblIsCoalesce
drop table tblIsNull
