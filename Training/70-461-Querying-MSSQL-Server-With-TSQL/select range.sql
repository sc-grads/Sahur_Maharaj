--if exists (select * from sys.procedures where name='NameEmployees')
if object_ID('NameEmployees','P') IS NOT NULL
drop proc NameEmployees
go
create proc NameEmployees(@EmployeeNumberFrom int, @EmployeeNumberTo int) as
begin
	if exists (Select * from tblEmployee where EmployeeNumber between @EmployeeNumberFrom and @EmployeeNumberTo)
	begin
		select EmployeeNumber, EmployeeFirstName, EmployeeLastName
		from tblEmployee
		where EmployeeNumber between @EmployeeNumberFrom and @EmployeeNumberTo
	end
end
go
NameEmployees 4, 5
execute NameEmployees 223, 227
exec NameEmployees @EmployeeNumberFrom = 323, @EmployeeNumberTo = 327

--if exists (select * from sys.procedures where name='NameEmployees')
if object_ID('NameEmployees','P') IS NOT NULL
drop proc NameEmployees
go
create proc NameEmployees(@EmployeeNumberFrom int, @EmployeeNumberTo int) as
begin
	if exists (Select * from tblEmployee where EmployeeNumber between @EmployeeNumberFrom and @EmployeeNumberTo)
	begin
		declare @EmployeeNumber int = @EmployeeNumberFrom
		while @EmployeeNumber <= @EmployeeNumberTo
		BEGIN
			if exists (Select * from tblEmployee where EmployeeNumber = @EmployeeNumber)
			select EmployeeNumber, EmployeeFirstName, EmployeeLastName
			from tblEmployee
			where EmployeeNumber = @EmployeeNumber
			SET @EmployeeNumber = @EmployeeNumber + 1
		END
	end
end
go
NameEmployees 4, 5
execute NameEmployees 223, 227
exec NameEmployees @EmployeeNumberFrom = 323, @EmployeeNumberTo = 1327
