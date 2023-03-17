declare @json NVARCHAR(4000)SET @json = '
{"name" : "Phillip",
 "ShoppingTrip":
	{"ShoppingTripItem": "L1",
	"Items":
	[
		{"Item":"Bananas", "Cost":5}, 
		{"Item":"Apples", "Cost":4}, 
		{"Item":"Cherries", "Cost":3} 
	]
	}}
'

--{"name":"Phillip", --This is an object. It is surrounded by curly braces {} name is the key, and Phillip is the value.
                     --It is in the format name colon value, then a comma before the next name.
--	"ShoppingTrip":
--	{"ShoppingTripItem": "L1",
--	"Items":
--	{"Item":"Bananas", "Cost":5} -- This is the Items value, and it is an object
--	}}

select isjson(@json)
select JSON_value(@json,'$."Name"')
--select JSON_value(@json,'strict $."Name"')
select JSON_value(@json,'strict $."name"')
select JSON_QUERY(@json,'$')
select json_value(@json,'strict $.ShoppingTrip.Items[1].Item')
select json_modify(@json,'strict $.ShoppingTrip.Items[1].Item','Big Bananas')
select json_modify(@json,'strict $.ShoppingTrip.Items[1]','{"Item":"Big Apples", "Cost":1}')
select json_modify(@json,'strict $.ShoppingTrip.Items[1]',json_query('{"Item":"Big Apples", "Cost":1}'))
select json_modify(@json,'$.Date','2022-01-1')
--select json_modify(@json,'strict $.ShoppingTrip.Items[1].Item','')
select * from openjson(@json)
select * from openjson(@json,'$.ShoppingTrip.Items')
select * from openjson(@json,'$.ShoppingTrip.Items')
	with (Item varchar(10), Cost int)

select 'Bananas' as Item, 5 as Cost
UNION
select 'Apples' as Item, 4 as Cost
UNION
select 'Cherries' as Item, 3 as Cost
for json path, root('MyShopping Trip')

