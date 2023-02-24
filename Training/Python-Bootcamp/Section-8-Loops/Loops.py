# for --> str, list, tup, set, and files are all iterable
for letter in 'Python':
    print('--->', letter)

# vowel check
my_str = 'test'  # --> input('Enter word: ')
vowels = 'aieou'

for v in my_str:
    if v in vowels:
        print(v, end=' ')
    else:
        print(my_str)

# Ranges
numbs = range(2, 10, 3)  # <-- min max step
print(list(numbs))  # <-- Prints as itr lst
sum_to = sum(range(1, 1001))
print(sum_to)

# loops and ranges
s = 0
for i in range(101):
    s += i
print(f'sum: {s}')

for _ in range(10):  # <-- _ is a throw var
    print('Still loops\n', _)

import random

names = ['abc', 'def', 'dede', 'zgrrgze', 'runner', 'matrix']
for _ in range(1, 4):
    print(f'Choosing winner. Round {_} ...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('-----------------')

# for continue and pass loops
for le in 'running':
    if le == 'i':
        continue
    print(le, end='')

for nu in range(10):
    if nu % 2 == 0:
        print(f'Even Number {nu}')
        continue
    print(f'Odd Numbers: {nu}')

pass  # <-- Placeholder
for _ in range(100):
    pass

# break Statements
for numb in range(10):
    print(numb)
    if numb == 5:
        break  # <-- Exits loop
    # exit()  # <-- Stops program completely
print('Broken out')

# While loops
x = 0
while x <= 10:
    print(f'X is: {x}')
    x += 1
print('ended while loop')

# while continue returns bak to start of the while loop
x = 12
while x < 100:
    x += 1
    if x % 13 != 0:
        continue
    print(x)

# while and break
while True:
    guess = int(input('Enter number between 1 - 10: '))
    if guess == 7:
        print(f'Winner: {guess}')
        break
    else:
        print(f'Try Again {guess}')

# prime number
a = int(input('Enter a number for prime check: '))
while a > 1:
    b = a // 2
    while b > 1:
        if a % b == 0:
            print(f'{a} is not prime')
            break
        b -= 1
    else:
        print(f'{a} is a prime number')
    a -= 1

# wallrus opperator syntax
# name := expression assigns expression to name
print(x := 2 + 4)
print(f'x is {x}')

value = input('Enter a str: ')
while value != '':
    print(f'Entered: {value}')
    value = input('Enter: ')

while (value := input('Enter: ')) != '':
    print(f'Entered: {value}')  # <-- does same as above
