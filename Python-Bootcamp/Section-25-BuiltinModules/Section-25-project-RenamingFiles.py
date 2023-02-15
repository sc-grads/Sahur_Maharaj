import os

os.chdir('C:\\Users\\Sahur Maharaj\\Downloads')
itr = 1
for file in os.listdir():
    name, ext = os.path.splitext(file)
    print(name, ext)
    new_name = f'{str(i)}-dlFile-{name}{ext}'
    print(new_name)
    itr += 1
    print('Renamed: ')
    os.rename(file, new_name)