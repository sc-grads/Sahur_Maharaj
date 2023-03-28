select [name]
from sys.all_columns

select [name] + 'A'
from sys.all_columns

select [name] + N'Ⱥ'
from sys.all_columns

select substring([name],2,len([name])-1) as [name]
from sys.all_columns

select substring([name],1,len([name])-1) as [name]
from sys.all_columns