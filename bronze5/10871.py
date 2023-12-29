a, b = map(int, input().split())
c = map(int, input().split())

d = list(c)

for i in d:
    if i < b:
        print(i, end=' ')