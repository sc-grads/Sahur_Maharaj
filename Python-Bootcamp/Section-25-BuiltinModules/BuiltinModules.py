import sys, os
stdout = sys.stdout
with open('out.txt', 'w') as sys.stdout:
    print('output redirection')
    help('sys')

sys.stdout = stdout

with open('out.txt') as f:
    pass# print(f.read())


# sys.argv run from cmd
print(f'Args: {len(sys.argv)}')
if len(sys.argv) >= 2:
    for i in sys.argv[1:]:
        with open(i, 'r') as f:
            print(f.read())

# os module
os.getcwd()
os.chdir('C:\\')
os.listdir()
os.path.getatime('out.txt')
x = max(os.listdir(), key=os.path.getatime)

# os.mkdir('dir1')
# os.mkdris('dir1\\dir2')
# os.__file__  # => '/usr/lib/python3.7/os.py'
#
# cwd = os.getcwd()  # => returns the current working directory
# print(cwd)
#
# ## changes the current working directory, OS specific
# os.chdir('/home/user1/python')  # Linux specific
# os.chdir('C:\\Users')  # Windows specific
#
# os.path.isfile('/etc/passwd')  # returns True if argument is a file
# os.path.isdir('/tmp')  # returns True if argument is a directory
#
# ## Splits the extension from a pathname, returns a tuple
# name, extention = os.path.splitext('/var/log/kern.log')  # name is 'kern', extention is '.log'
#
# ## Listing a directory
# os.listdir('.')  # returns the entries in the current working directory as a list
# os.listdir('C:\\Users')  # returns the entries in the directory as a list
#
# os.path.getmtime('/etc/passwd')  # => 1547047769.9049096, returns file's last modification time as a timestamp
# os.path.getsize('/etc/passwd')  # => 2691, returns the size of a file
#
# os.mkdir('PATH/dir')  # creates a new directory in PATH, os specific
#
# ## Creates a new directory called dir1 in Windows (permissions required)
# os.mkdir('C:\\dir1')
#
# ## Creates a new directory called dir1 in Linux
# os.mkdir('~/dir1')


# Shutil  <-- Shell utilities
import shutil as sh
sh.copyfile('src','dest')  # <-- cpy content not data
sh.copy()  # <-- copies meta data
sh.copy2() # <-- copies over
sh.copytree()  # recursive copy
sh.move()  # <--move or rename

