# YOUR CODE STARTS HERE
with open('a.txt', 'r') as f:
    f.seek(4)
    word = f.read(5)
    print(word)
