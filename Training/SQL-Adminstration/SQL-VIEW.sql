CREATE VIEW vw_mrPhone AS
SELECT TOP (100) PERCENT Person.Person.Title, Person.Person.FirstName, Person.Person.LastName, Person.PersonPhone.PhoneNumber, Person.PhoneNumberType.Name AS PhoneType
FROM Person.Person INNER JOIN
Person.PersonPhone
ON Person.Person.BusinessEntityID = Person.PersonPhone.BusinessEntityID
INNER JOIN
Person.PhoneNumberType
ON Person.PersonPhone.PhoneNumberTypeID = Person.PhoneNumberType.PhoneNumberTypeID
WHERE (Person.Person.Title = N'Mr.')
ORDER BY Person.Person.FirstName DESC
------------------------
SELECT * FROM vw_mrPhone WHERE PhoneType = N'work'

