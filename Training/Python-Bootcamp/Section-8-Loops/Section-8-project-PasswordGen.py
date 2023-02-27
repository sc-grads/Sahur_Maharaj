# Pass Gen
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
print(random.choice(chars))
pass_len = int(input('Enter password length: '))
passwd = ''

for _ in range(pass_len):
    c = random.choice(chars)
    passwd += c
print(f'Your password is: {passwd}')
