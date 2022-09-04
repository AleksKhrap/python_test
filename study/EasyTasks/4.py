a = int(input('a: '))
if abs(a) > 10000:
    print('Error!')
else:
    print('The next number for the number ', a, ' is ', a+1, '.', sep='')
    print('The previous number for the number ', a, ' is ', a-1, '.', sep='')
