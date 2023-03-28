DECLARE @chars AS CHAR(10)
SET @chars = 'Hell0'
SELECT @chars, len(@chars), DATALENGTH(@chars)

DECLARE @Vchars AS VARCHAR(10)
SET @Vchars = 'Hell0'
SELECT @Vchars, len(@Vchars), DATALENGTH(@Vchars)


DECLARE @nchars AS NCHAR(10)
SET @nchars = N'Hell0»'
SELECT @nchars, len(@nchars), DATALENGTH(@nchars)

DECLARE @NVchars AS NVARCHAR(30)
SET @NVchars = N' Hell0♥¢     '
SELECT @NVchars, len(@NVchars), DATALENGTH(@NVchars)


SELECT LEFT(@Nchars, 2), RIGHT(@Nchars, 2)
SELECT SUBSTRING(@Nchars, 1, 3)

SELECT LTRIM(@NVchars), RTRIM(@NVchars)
SELECT REPLACE(@nchars, 'l','e')