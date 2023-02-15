salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}

# YOUR CODE STARTS HERE
tax = {k: v * 0.1 for k, v in salaries.items()}
print(tax)