 
CREATE PROCEDURE [dbo].[SelectAllPersonAddress]
AS
SELECT * FROM  Person.Address
go;

GO


-----------------------

exec [dbo].[SelectAllPersonAddress]

-------------------------------------------------

drop procedure [dbo].[SelectAllPersonAddressWithParams]

----------------
CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParams] (@City NVARCHAR(30))
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO



--------------------------

exec SelectAllPersonAddressWithParams @city = 'New York'

-------------------------------

exec SelectAllPersonAddressWithParams 'Miami'

----------------------------------

drop procedure [SelectAllPersonAddressWithParams]

--------------------------

CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParams] (@City NVARCHAR(30) = 'New York')
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO


-------------------

exec SelectAllPersonAddressWithParams 'Miami'

------------------------------------------

CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParams] (@City NVARCHAR(30) = 'New York',@stateProvinceid int)
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO


----------------------

CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParamswithEncryption] (@City NVARCHAR(30) = 'New York',@stateProvinceid int)
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO


-----------------------------------------------
