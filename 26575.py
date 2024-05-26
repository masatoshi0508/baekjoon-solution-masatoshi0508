n = int(input())

for _ in range(n):
    d, f, p = map(float, input().split())
    print("$" + '{:.2f}'.format(d*f*p))