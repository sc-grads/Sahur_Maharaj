#1. Create a list called nums_list with the items: 'a', 3, 5.5, 'a', 4
nums_list = ['a', 3, 5.5, 'a', 4]
print(nums_list)

#2. Create a tuple called nums_tuple from the nums_list using the tuple() constructor.
nums_tuple = tuple(nums_list)
print(nums_tuple)

#3. Create a set called nums_set from the nums_list using the set() constructor. Print the set.
nums_set = set(nums_list)
print(nums_set)


#4. Given the following list, create a new list called unique_ip that contains only unique values in the ip list.
# Print the unique_ip list.
ip = ['10.0.0.1', '10.0.0.2', '10.0.0.1', '10.0.0.3', '10.0.0.1', '10.0.0.2']   # DO NOT MOFITY THIS LINE

unique_ip = list(set(ip))
print(unique_ip)
