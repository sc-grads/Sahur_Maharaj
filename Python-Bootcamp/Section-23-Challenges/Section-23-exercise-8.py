message = 'Wow! Python is great'
vowels = 'aeio'

# YOUR CODE STARTS HERE
no_vowels = [v for v in message if v not in vowels and v != ' ']
print(no_vowels)
