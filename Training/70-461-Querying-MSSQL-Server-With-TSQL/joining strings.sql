declare @fName nvarchar(50)
declare @lName nvarchar(50)

SET @fName = 'SAD'
SET @lName = 'DAM'

SELECT @fName + @lName AS fullname
