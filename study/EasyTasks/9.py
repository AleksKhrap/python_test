n = int(input('n='))
if 11 <= n % 100 <= 14:
    print(n, 'korov')
else:
    temp = n % 10
    if temp == 0 or (5 <= temp <= 9):
        print(n, 'korov')
    if temp == 1:
        print(n, 'korova')
    if 2 <= temp <= 4:
        print(n, 'korovy')
