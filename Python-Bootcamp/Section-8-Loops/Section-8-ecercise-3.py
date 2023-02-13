## YOUR CODE STARTS HERE:
# Start a while loop that calculates the sum of odd numbers from 1 to 100.
# Use my_sum variable to save the value
my_sum = 0
ittr = 100
while ittr:
    ittr -= 1
    if ittr % 2 == 0:
        continue
    else:
        my_sum += ittr

print(my_sum)
