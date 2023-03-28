
CREATE TRIGGER tr_dpt1
    ON dbo.tblDepartment
    AFTER DELETE, INSERT, UPDATE
    AS
    BEGIN
	SELECT * FROM inserted
	SELECT * FROM deleted
    SET NOCOUNT ON
	select * from tblDepartment
	set nocount off
    END
	GO

	Create TRIGGER testr
	ON tblDepartment
	INSTEAD OF DELETE, INSERT
	AS
	BEGIN
	SET NOCOUNT ON
	END

