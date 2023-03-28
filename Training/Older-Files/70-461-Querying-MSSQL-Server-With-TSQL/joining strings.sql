declare @fName nvarchar(50)
declare @lName nvarchar(50)

SET @fName = 'SAD'
SET @lName = 'DAM'

SELECT @fName + @lName AS fullname

SELECT 'My num is: ' + try_cast(212 as char(10))

SELECT 'SAL IS: ' + FORMAT(2000.23, 'C', 'en-ZA')