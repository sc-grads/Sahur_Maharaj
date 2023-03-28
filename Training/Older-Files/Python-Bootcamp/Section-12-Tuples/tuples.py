# Tuples are immutable anc cannot be changed must have more than 1 value
# they are orderd sequences
t1 = tuple() # Empty
t2 = () # empty

t3 = (1, 3.4, 'python', True)
t4 = (10)  # <-- Not a Tuple
t4 = (10, )  # <-- Tuple

t5 = 6.5, True  # <-- also a tuple
t6 = tuple([1, 2, 3, 4, 5])
l1 = list(t5)

print(t5[0])

# tuple operation
my_tup = (1.4, 10, 'X', True, 10, 10 ,20, 10)
t1 = my_tup + tuple('ytS$')
print(t1)
t2 = (2, 3, 2) * 4
print(t2)

# slicing returns a new tuple
print(my_tup[0:2])
for i in my_tup:
    print(i)

print(310 in my_tup)

# Tuple Methods
tup_size = my_tup.count(10)
tup_ind = my_tup.index(10)  # <-- Returns first occurance
print(tup_size, tup_ind)

# Common methods work

# tups vs lists
# faster and more efficient than lists
# data that wont change use a tuple i.e: co-ordis / const
# safer than lists  cant accidently be changed
# tups can be keys in dicts
# Storage efficiency

l1 = [1, 2, 3, 4, 5, 6]
tup_new = (1, 2, 3, 4, 5, 6)

# see memory
import sys
print(f'list size {sys.getsizeof(l1)}')
print(f'tup size {sys.getsizeof(tup_new)}')

