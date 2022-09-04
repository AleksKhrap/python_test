n = int(input('Enter the number: '))
k = 0
if n > 100:
    print('Error')
else:
    for i in range(n+1):
        i *= i
        k += i
    print(k)
