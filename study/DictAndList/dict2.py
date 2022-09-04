from collections import Counter
a = input()
d = dict(Counter(a))
for key, value in d.items():
    print(key, value, sep=' - ')
