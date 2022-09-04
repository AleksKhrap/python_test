n = int(input('First number: '))
k = 0
if n >= 0:
    for i in range(0, n):
        if i % 2 == 0 and i % 7 == 0:
            k += 1
        print(k)
