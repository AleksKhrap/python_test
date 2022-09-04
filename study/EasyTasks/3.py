a = int(input())
b = int(input())
if a < 0 or b < 0 or a > 1000 or b > 1000:
    print('Error!')
else:
    print((a**2+b**2)**(1/2))
