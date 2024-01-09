n = int(input())
lis = map(int, input().split())

a = list(lis)
b = sum(a)

if b == 1:
    print('Right')
elif b == 0:
    print('Stay')
else:
    print('Left')