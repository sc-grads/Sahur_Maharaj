# Write a function called get_vat() with 2 parameters, price and vat percentage
# It calculates and returns the VAT (value-added tax).
# YOUR CODE STARTS HERE
def get_vat(price, percentage):
    total = price * (percentage / 100)
    return total


# Capture the returned value in a new variable called vat.
print(get_vat(200, 5))
