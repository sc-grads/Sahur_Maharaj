# opening files
f = open('ignoretxtfiles/configuration.txt', 'rt')  # <-- valid abs / relative path common open as read / write / append
# text mode
# binary mode
# text files stuctured as sequence of lines lines ended with eol (end of line)
# binary files unique files require spesific applications

content = f.read()  # <-- prints as string
print(content)
content = f.read(5)  # <-- read first 5 chars memorieses cursor location
print(content)
print(f.tell())
f.seek(3)
content = f.read(3)
print(content)
print(f.closed)
f.close()  # <-- use when done with the file
print(f.closed)

# absoloute paths throw errors due to backslashes to fix use escape char \ or use r for raw string format
# open with
print('#' * 50)

with open('ignoretxtfiles/configuration.txt') as f:
    cont = f.read()
print(cont)
print(f.closed)

print('#' * 50)
# read in to list
with open('ignoretxtfiles/configurationtolst.txt') as f:
    c = f.readlines()  # read().splitlines()
    print(c)

# writing to a file
with open('ignoretxtfiles/written.txt', 'w') as f:
    f.write('Written')
    f.write('\nNewline')

with open('ignoretxtfiles/written.txt', 'a') as f:
    f.write('adds not overrides')
