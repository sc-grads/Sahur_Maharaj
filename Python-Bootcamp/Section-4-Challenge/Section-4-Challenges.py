# Challenge 1
# A
num = 1  # <-- int
price = 12.23  # <-- float
is_active = False  # <-- bool
user_name = 'this is my name'  # <-- str
nums = [1, 3, 2, 4, 6]  # <-- list
# B
print(f'int: {num}\nfloat: {price}\nboolean: {is_active}\nstring: {user_name}\nlist: {nums}')
# ----------------------------------------------------------------------------------------------------
# Challenge 2
my_name = 'Andrei'
value = 100

# This is
# an example of a multiline
# comment in Python.


my_str = 'Hello'
print(my_str)
# ----------------------------------------------------------------------------------------------------
# Cahllenge 3
best_friend = 'Anne'
print('My best friend is ', best_friend)

age = 18
print(age == 10)

a, b = '10', '20'
print(a + b)

print('To comment a line of code you # at the beginning of the line.')
# ----------------------------------------------------------------------------------------------------
# Challenge 4
a = 10
b = 50

print(a == b)
print(a >= b)
print(a * b)
print(b ** a)
print(b / a)
print(a // b)
print(b % a)
a += 2
print(a)
b *= 2
print(b)
# ----------------------------------------------------------------------------------------------------
# Challenge 5
a = (16 / (2 + 6) / 2) ** 2
print(a)
# ----------------------------------------------------------------------------------------------------
# Challenge 6
total_ipv6 = 128 ** 2
print(total_ipv6)
# ----------------------------------------------------------------------------------------------------
# Challenge 7
total_revenu = 45_897_513
profit_rate = 12.7 / 100
total_profit = total_revenu * profit_rate
print(f'The Companies total profit is {round(total_profit, 2)}')
# ----------------------------------------------------------------------------------------------------
# Challenge 8
from math import isclose

a = 0.1
b = 0.3
ans = a * 3
print(isclose(ans, b, abs_tol=0))
# ----------------------------------------------------------------------------------------------------
