# try exept finally
try:
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    c = a / b
    print(c)
except ZeroDivisionError as err:  # other err types TypeError, Exception
    print('Errror has occured')
finally:
    print('default')

print('Code continued')

# python includes builtin exeptions for spesification