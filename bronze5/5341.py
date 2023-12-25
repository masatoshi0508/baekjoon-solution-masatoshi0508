while True:
    total = 0
    n = int(input())
    if n == 0:
        break
    for i in range(1, n+1):
        total += i
    print(total)