# Conditionals
bal = 100
price = 50

if bal >= price:
    new_bal = bal - price
    print(f'You can book the flight and the account new balance will be {new_bal}')
else:
    print(f'No Funds please add {price - bal}')

# Elif --> Can Be nested
answer = input('Enter yes or no').lower()
if answer == 'yes':
    if bal >= 12:
        print(True)
    else:
        print('Bal less than 12')
elif answer == 'no':
    print(False)
else:
    print('Error')

# Booleans and or not
result = ''
if result:
    print('Not empty')
else:
    print('Empty')

age = 6
if 0 < age <= 18:
    print('Too young')
elif age > 0 or age <= 10:
    print('Younger')
elif age != 6:
    print('Age not 6')
elif age == None:
    print('Age is None')
else:
    print('Unknown')

# short circut eval
a, b = 20, 30
print(f'{a > b and b == 20}')  # <-- will skip val on left if right is true
