# List of Words
words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom' ]

# YOUR CODE STARTS HERE

palindromes  = [p for p in words if p.lower() == p[::-1].lower()]
print(palindromes )