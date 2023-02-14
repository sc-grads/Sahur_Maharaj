# YOUR CODE STARTS HERE

file = open('ip.txt', 'r')
ip_list = list(file.read().split('\n'))

print(ip_list, end='')
file.close()