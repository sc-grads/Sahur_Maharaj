##############################
## The decimal module
##############################

## Importing the module
import decimal
from decimal import Decimal

## There is no exact representation for some float numebers. We can't use arithmetic operators with some floats
a = 0.3
# a displayed with 25 decimal points
print(format(a, '.25f'))  # => 0.2999999999999999888977698
print(a * 3 == 0.9)  # => False

## Creating a integer using the Decimal class
## The argument is an integer or a string
x = Decimal(5)
y = Decimal('5')
print(x == y)  # => True

## Creating a float using the Decimal class
## The argument should be the float as a string
x = Decimal(0.3)  # WRONG!
y = Decimal('0.3')  # CORRECT!
z = Decimal('0.9')

print(x == y)  # => False
print(y * 3 == z)  # => True

## There are methods in the Decimal class that should be used instead of methods from the maths module
x = Decimal(0.3)
sq = x.sqrt()
print(format(sq, '.20f'))  # => 0.54772255750516610332

import math

sq = math.sqrt(0.3)
print(format(sq, '.20f'))  # => 0.54772255750516607442

## Getting the context
print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0,
# flags=[FloatOperation], traps=[InvalidOperation, DivisionByZero, Overflow])

print(decimal.getcontext().prec)  # => 28
print(decimal.getcontext().rounding)  # => ROUND_HALF_EVEN

## Chainging the precision and the rounding
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN