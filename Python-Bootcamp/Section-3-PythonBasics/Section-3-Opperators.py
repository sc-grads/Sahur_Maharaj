# Basic python operators
"""
Arithmetic Operators: + - * / // ** %
Assignment Operators: = += -= *= /=
Comparison Operators: == != > >= < <=
Identity Operators: "is" "is not"
Logical Operators: "and" "or" "not"
"""

# order of opers --> **, *, /, +, -
x = 10
a = 11.1
b = 3

print(x + a)
print(x - b)
print(x / 2)
print(x % 2)  # <-- gives the remainder value
print(x ** 2)  # <-- exponent

# seperate large digits using comma or underscores
print(1_000 == 1000)

# assignment operators
s = 5
print(s)
s += 2  # <-- adds 2 to s
print(s)
s -= 3  # <-- minus 3 from s
print(s)
s *= 2  # <-- multiply s by 2
print(s)
s /= 3  # <-- divide s by 3
print(s)
s **= 5  # <-- s pow 5
print(s)
s %= 2  # <-- remainder of s / 2
print(s)

# increment and decrement
s += 1
s -= 1

# divmod function find quotien and remainder
r, t = divmod(14, 6)
print(r, t)  # 2 remainder 2

# pow <-- power function
print(pow(5, 9))

# sum
print(sum(4, 2, 2, 2, 4))

# max
print(max(4, 2, 2, 2, 4, 9))

# min
print(min(4, 2, 2, 2, 4, -10))

# round
PI = 3.14159
print(round(PI, 2))
# the comparisons returning true or false ==, !=
print(f'This is true {7 == 7} and this is false {7 != 7}')

# <=, >=
print(f'{6 >= 7} is true and {8 <= 9} is false')

# ident opperators -> [is and is not] these operators compare addresses in memory

a, b = 3, 'a'

z = a is b
print(z)

# The value of a mutable variable can be changed after it has been created,
# but the value of an immutable variable can’t be changed.

# Immutable types: ints, floats, strs, tups, frozenset
# mutable types: list, sets, dicts

print(a)  # <-- a is immutable as the address has changed
print(id(a))  # view mem address
a += 3  # memory address changed
print(id(a))
print(a)

nums = [1, 2, 3]  # <-- nums is mutable as the address has NOT changed
print(id(nums))  # view mem addr
nums.append(1223)  # Add value to end of list
print(id(nums))  # memory address is the same
