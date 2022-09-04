n = int(input())
dict = {}

for _ in range(n):
    k, v = input().split()
    dict[k] = v

synonim = input()

print(dict.get(synonim) or ''.join([k for k, v in dict.items() if v == synonim]) or 'No synonim')