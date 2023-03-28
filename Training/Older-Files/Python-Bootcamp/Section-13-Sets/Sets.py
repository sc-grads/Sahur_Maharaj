# Sets
s1 = {1, 2, 3, 'a', 3, 'b'}
print(s1)  # <-- Unorderd list changes on runtime unable to acces via index --> Removes Dupliucates

# sets can be modified they are mutable
s1.add((10, 33))
print(s1)
s1.remove('a')
print(s1)

# elements can be immutable only
s2 = set('helllo')
print(s2)
s3 = set((123122, 'a', 303))
print(s3)
s4 = set([21, 3, 21, 4, 3, 22, 1])
print(s4)

macs = ['F4-D1-08-CA-CD-34', 'F4-D1-08-CA-CD-34', 'F4-D1-08-CA-CD-33']
uniq_mac = list(set(macs))  # <-- converted to list
print(uniq_mac)
print(len(uniq_mac))

for i in s4:
    print(i)
# set methods
s1 = {1, 2, 3, 3, 4, 5, 6, 6}
s2 = {2, 3, 1}
print(s1 == s2)
print(s1 is s4)

s1.add(3)
s1.add('a')
print(s1)
# method does nothiong if item exists

# removing
s1.remove(3)  # remove first throw error if element doesnot exist
s1.discard('x')  # no error
pop1 = s1.pop()  # remove and return elemnt reanomly
print(pop1, s1)

s1.clear()
s4 = s1.copy()
s4.add(2342)
print(s4, s1)

# new examples
s1 = {1, 3, 5}
s2 = {5, 7, 3}
# intersection
s3 = s1.intersection(s2)
print(s3) #  <-- new set
s3 = s1 & s2  # <-- same as intersect
# Diffrence
s4 = s1.difference(s2) # can use - s4 = s1 - s2
print('Here', s4)
# symetric diffrence
s5 = s1.symmetric_difference(s2)
print(s5)
# Union
s6 = s1.union(s2)
print(s6)

# sets are implemented as hash tables --> time complexity is constant
# time complexity
import time, sys
l1 = list(range(1_000_000))
startl1 = time.time()
print(startl1)
bv = 4974875 in l1
endl1 = time.time()
print(endl1 - startl1)
# time complexity for sets
print('#' * 25)
s1 = set(range(1_000_000))
starts1 = time.time()
srch = 549849 in s1
ends1 = time.time()
print(ends1 - starts1)

# sets consume more memory
print(sys.getsizeof(l1))
print(sys.getsizeof(s1))

# frozen sets are immutable but have same properties as sets --> can be used as id
fs1 = frozenset({1,2,3,4,5,6,'a','c'})
print(fs1)
fs2 = frozenset('Python')
print(fs2)
print(fs2.symmetric_difference(fs1))


