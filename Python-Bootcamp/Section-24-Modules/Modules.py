# modules are imported files
import sys
import math, random, time
import threading as th
from io import *
from math import pow

print(math.factorial(333))
print(th.TIMEOUT_MAX)
print(math.pi)
print(sys.path)

help('modules')
# #########################
# ##Importing Python Modules
# #########################
#
# ## Importing a module
# import math
#
# ## Importing two or more modules
# import sys, os
#
# ## Importing a module as an alias
# import random as r
#
# ## Importing just the Response class from requests module
# from requests import Response
#
# ## Importing a class from a module as an alias
# from requests import Response as res
#
# ## Import everyting directly from shutil module into the global namespace
# ## TO BE AVOIDED!
# from shutil import *
#
# ## The block of code below if will be executed only when the script is run directly (not imported in another script)
# if __name__ == '__main__':
#     print('Running the script directly. Not importing it as a module.')


# creating modules
import math_module
math_module.a = 222
print(f'math mod a: {math_module.a}')
total = math_module.add_a(1, 2, 34, 5)
print(total)
print(f'__name__ in modules is: {__name__}')
