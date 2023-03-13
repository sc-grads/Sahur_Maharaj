CREATE TABLE tblSecond(
	myNumbers INT
)
GO
INSERT INTO tblSecond VALUES
	(253),
	(654),
	(5465),
	(45)
GO

SELECT * FROM dbo.tblFirst
SELECT myNumbers FROM dbo.tblSecond

DELETE FROM tblSecond  -- DELETES CONTENT OF TABLE
TRUNCATE TABLE tblSecond

DROP TABLE tblFirst  -- DELETES TABLE
