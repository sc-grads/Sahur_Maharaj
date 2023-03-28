# List with duplicates
mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']

# YOUR CODE STARTS HERE
mac_unique = []
for i in mac:
    if i not in mac_unique:
        mac_unique.append(i)

print(mac_unique)