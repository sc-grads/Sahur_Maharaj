# try exept finally
try:
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    c = a / b
    print(c)
except:
    print('Errror has occured')
finally:
    print('default')

print('Code continued')