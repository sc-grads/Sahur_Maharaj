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

