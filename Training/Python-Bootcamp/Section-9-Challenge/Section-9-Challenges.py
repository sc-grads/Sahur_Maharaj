# Challenge 1
c1_num = int(input('Enter a Number:'))
divisors = list()
for i in range(2, c1_num // 2 + 1):
    if c1_num % i == 2:
        divisors.append(i)
print(divisors)
# =====================================================================================================================
# Challenge 2
x = int(input('Enter x: '))
y = int(input('Enter y: '))
is_power = False
for z in range(2, x // 2):
    if y ** z == x:
        print(f'{y} ** {z} = {x}')
        is_power = True
        break
else:
    print(f'{x} is not a power of {y}')
# =====================================================================================================================
# Challenge 3
count = 0
vowels = 'aeiou'
search_me = 'The Quick Brown Fox Jumped Over The Lazy Dog.'
for vo in vowels:
    if vo in search_me.lower():
        count += search_me.count(vo)
print(f'Vowels in the string {search_me} are \n {count}')
# =====================================================================================================================
# Challenge 4
side_1 = int(input('Enter side 1: '))
side_2 = int(input('Enter side 2: '))
side_3 = int(input('Enter side 3: '))
if side_1 == side_2 == side_3:
    print('equilateral Triangle')
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print('isosceles Triangle')
else:
    print('Scalene Triangle')
# =====================================================================================================================
# Challenge 5
sum_num = 0
prod_num = 1
avg_counter = 0
while True:
    numb = float(input('Enter a Number to get product, sum and average: '))
    if numb == 0:
        break
    else:
        sum_num += numb
        prod_num *= numb
        avg_counter += 1
print(f'the sum is {sum_num} \nthe product is {prod_num} \nthe average is {sum_num / avg_counter}')
# =====================================================================================================================
# Challenge 6
s1 = 'Python31py50'
sum_str = 0
avg_initzr = 0
for c in s1:
    if c.isdigit():
        sum_str += int(c)
        avg_initzr += 1
print(f'sum {sum_num}\naverage {sum_str / avg_initzr}')
# =====================================================================================================================
# Challenge 7
tab_to_10 = int(input('Enter number to multiply to 10: '))
for t in range(1, 11):
    print(f'{t} X {tab_to_10} = {tab_to_10 * t}')
# =====================================================================================================================
# Challenge 8
num = int(input('Enter number for recurse: '))
for elemn in range(num + 1):
    print(str(elemn) * elemn)
# =====================================================================================================================
# Challenge 9
s2 = 'test'
s3 = 'easter'
c_char = ''
for chr1 in s2:
    if chr1 in s2:
        if chr1 not in c_char:
            c_char += chr1
print(f'commons: {c_char}')
# =====================================================================================================================
# Challenge 10
for foobar in range(51):
    if foobar % 3 == 0 and foobar % 5 == 0:
        print('FooBar')
        continue
    if foobar % 3 == 0:
        print('Foo')
        continue
    elif foobar % 5 == 0:
        print('Bar')
        continue

    print(foobar)
# =====================================================================================================================
# Challenge 11
fibb_to = int(input('Enter number to Fibonacci: '))
start_pt, cont_pt = 0, 1
while start_pt <= fibb_to:
    print(start_pt, ' ', end=', ')
    start_pt, cont_pt = cont_pt, start_pt + cont_pt
# =====================================================================================================================
# Challenge 12
rows = 10
for i in range(rows):
    for star in range(i):
        print('*', end='')
    print(' ')
# =====================================================================================================================
