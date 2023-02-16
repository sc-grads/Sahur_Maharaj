import math, threading as th
import math_module

print(math.factorial(3))
print(th.TIMEOUT_MAX)
print(math.pi)

# help('modules')

# creating modules
math_module.a = 222
print(f'math mod a: {math_module.a}')

total = math_module.add_a(1, 2, 34, 5)
total2 = math_module.sqrt(2)
print(total2)
print(total)
print(f'__name__ in modules is: {__name__}')
