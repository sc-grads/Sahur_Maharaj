create proc NameEmployees as
begin 
	select EmployeeNumber, EmployeeFirstName, EmployeeLastName
	from tblEmployee
end
go
NameEmployees
execute NameEmployees
exec NameEmployees
--if exists (select * from sys.procedures where name='NameEmployees')
if object_ID('NameEmployees','P') IS NOT NULL
drop proc NameEmployees
go
create proc NameEmployees(@EmployeeNumber int) as
begin
	if exists (Select * from tblEmployee where EmployeeNumber = @EmployeeNumber)
	begin
		select EmployeeNumber, EmployeeFirstName, EmployeeLastName
		from tblEmployee
		where EmployeeNumber = @EmployeeNumber
	end
end
go
NameEmployees 
execute NameEmployees 223
exec NameEmployees 323
select EmployeeNumber from NameEmployees

DECLARE @EmployeeName int = 123
select @EmployeeName
