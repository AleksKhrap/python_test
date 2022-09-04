n, k = [int(x) for x in input().split()]
a = ['I'] * n
for i in range(k):
    left, right = [int(x) for x in input().split()]
    for j in range(left - 1, right):
        a[j] = '.'
print(''.join(a))
