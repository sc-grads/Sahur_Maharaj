# Data structure --> organsed process retrive and store data

l1 = [1, 2.5, 'Python', True, [1, 'abc', 'der'], (10, 10, 20)]  # <-- Can hold multipe types
l2 = []  # empty
l3 = list()  # empty

print(len(l1))
print(l1[0])
x = l1[-1]
print(x)

# lists are mutable the elements can be modified without creating a new list
l4 = list('abcd')
print(id(l4))
l4[0] = 'X'
l4.append(10001)
print(l4)
print(id(l4))

# list concats
l1 = [3, 4]
print(id(l1))
l1 = l1 + [5, 6]
print(id(l1))  # <-- Changes id
print(l1)
l1 += [7, 8]
print(id(l1))  # <-- Does not id
print(l1)
l1.extend([11, 12])  # <-- adds multiple values
print(l1)
l1.append(['a', 'b'])  # <-- Adds Single value
print(l1)

# repetition
l2 = list('abcde')
l3 = l2 * 3
print(l2)


# slicing
print('#' * 10 + ' List Slicing ' + '#' * 10)
numbers = [1, 3, 2, 4, 5]
nums = numbers[1:4]  # <-- Returns new list
print(nums)
print(numbers)
print(numbers[:3])
print(numbers[2:])
print(numbers[4:1:-2])
print(numbers[::-1])  #  <-- reverse list

# ittr
ip_lst = ['192.168.1.2', '127.0.0.1', '10.0.0.1']
for ip in ip_lst:
    print(f'Connecting to {ip}')
    print('127.1.1.0' in ip_lst)

# List methods
l1 = list()
print(dir(l1))
help(l1.extend)

# append adds 1 element
l1.append(2)
print(l1)
# extend adds itr obj to list
l1.extend([5, 10, 40])
print(l1)
# insert add element at index
l1.insert(1, 20)
print(l1)

# remove
l1.clear()  # <-- removes all elements
print(l1)
l1 = [1, 2, 4, 5, 4, 4, 2, 2, 1, 4]
l1.pop(2)  # <-- remove last element by default
print(l1)
l1.remove(5)
print(l1)

# get index
print(l1.index(1))
# count elements
print(l1.count(4))
# reverse
l1.reverse()
print(l1)
# sort
l1.sort()
print(l1)
print(sorted(l1))  # <-- returns new list
l1.sort(reverse=True)
print(l1)
print(max(l1), min(l1), sum(l1))

# str methods split and join
s1 = 'Hello python'
l1 = s1.split()  # <-- space tab nd new line as default seperator
l2 = s1.split('p')
print(l1)
print(l2)
# join list
ip_str = ', '.join(ip_lst)
print(ip_str)

# List Comprehension
clicks = [10, 5, 15, 43]
double_c = []

for c in clicks:
    double_c.append(c*2)
print(double_c)

# Better way
tripe_c = [c*3 for c in clicks]
print(tripe_c)

friends = ['a1', 'b23', 'c3432', 'harry', 'paul']
reversed_names = [i[::-1] for i in friends]
print(reversed_names)

nums = [1, 3, 4, 65, 3, 2]
divi_by_seven = [n for n in nums if n % 7 == 0]
print(divi_by_seven)

nums_2 = [str(n) for n in nums]
print(nums_2)
print('-'.join(nums_2))

# Example
fri = ['jhon', 'dan', 'marry']
fri_l = [na.lower() for na in fri]
neig = ['tim', 'dan', 'marry']
neig_l = [ne.lower() for ne in neig]
fri_nei = [na.lower() for na in fri_l if na in neig_l]
print(fri_nei)

