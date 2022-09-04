a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
if a != 0:
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + d**(1/2)) / (2 * a)
        x2 = (-b - d**(1/2)) / (2 * a)
        print(x1)
        print(x2)
    elif d == 0:
        x1 = (-b + d**(1/2)) / (2 * a)
        print(x1)
    else:
        print('Корней нет!')
else:
    print('Неверное значение a!')
