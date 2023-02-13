language ='$Python$$'
message = 'I love Python!'

# YOUR CODE STARTS HERE:
language1 = language.strip('$')
language2 = language1.lower()

message1 = message.upper()
message2 = message.replace('Python', 'Java')

print(language1)
print(language2)
print(message1)
print(message2)
