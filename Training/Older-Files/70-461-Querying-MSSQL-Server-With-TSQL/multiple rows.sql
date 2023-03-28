alter TRIGGER tr_ViewByDepartment
ON dbo.ViewByDepartment
INSTEAD OF DELETE
AS
BEGIN
    declare @EmployeeNumber as int
	declare @DateOfTransaction as smalldatetime
	declare @Amount as smallmoney
	select @EmployeeNumber = EmployeeNumber, @DateOfTransaction = DateOfTransaction,  @Amount = TotalAmount
	from deleted
	--SELECT * FROM deleted
	delete tblTransaction
	from tblTransaction as T
	where T.EmployeeNumber = @EmployeeNumber
	and T.DateOfTransaction = @DateOfTransaction
	and T.Amount = @Amount
END

begin tran
SELECT * FROM ViewByDepartment where EmployeeNumber = 132
delete from ViewByDepartment
where EmployeeNumber = 132
SELECT * FROM ViewByDepartment where EmployeeNumber = 132
rollback tran

-- Good code - allows multiple rows to be deleted

alter TRIGGER tr_ViewByDepartment
ON dbo.ViewByDepartment
INSTEAD OF DELETE
AS
BEGIN
	SELECT *, 'To Be Deleted' FROM deleted
       delete tblTransaction
	from tblTransaction as T
	join deleted as D
	on T.EmployeeNumber = D.EmployeeNumber
	and T.DateOfTransaction = D.DateOfTransaction
	and T.Amount = D.TotalAmount
END
GO

begin tran
SELECT *, 'Before Delete' FROM ViewByDepartment where EmployeeNumber = 132
delete from ViewByDepartment
where EmployeeNumber = 132 --and TotalAmount = 861.16
SELECT *, 'After Delete' FROM ViewByDepartment where EmployeeNumber = 132
rollback tran
