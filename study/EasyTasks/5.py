a = int(input('a: '))
if a > 999 or a < 100:
    print('Error!')
else:
    print(sum(map(int, str(a))))
