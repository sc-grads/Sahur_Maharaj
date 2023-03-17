--if exists (select * from sys.procedures where name='NameEmployees')
if object_ID('NameEmployees','P') IS NOT NULL
drop proc NameEmployees
go
create proc NameEmployees(@EmployeeNumberFrom int, @EmployeeNumberTo int, @NumberOfRows int OUTPUT) as
begin
	if exists (Select * from tblEmployee where EmployeeNumber between @EmployeeNumberFrom and @EmployeeNumberTo)
	begin
		select EmployeeNumber, EmployeeFirstName, EmployeeLastName
		from tblEmployee
		where EmployeeNumber between @EmployeeNumberFrom and @EmployeeNumberTo
		SET @NumberOfRows = @@ROWCOUNT
		RETURN 0
	end
	ELSE
	BEGIN
	    SET @NumberOfRows = 0
		RETURN 1
	END
end
go
DECLARE @NumberRows int, @ReturnStatus int
EXEC @ReturnStatus = NameEmployees 4, 5, @NumberRows OUTPUT
select @NumberRows as MyRowCount, @ReturnStatus as Return_Status
GO
DECLARE @NumberRows int, @ReturnStatus int
execute @ReturnStatus = NameEmployees 4, 327, @NumberRows OUTPUT
select @NumberRows as MyRowCount, @ReturnStatus as Return_Status
GO
DECLARE @NumberRows int, @ReturnStatus int
exec @ReturnStatus = NameEmployees @EmployeeNumberFrom = 323, @EmployeeNumberTo = 327, @NumberOfRows = @NumberRows OUTPUT
select @NumberRows as MyRowCount, @ReturnStatus as Return_Status
