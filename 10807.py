a = int(input())
b = map(int, input().split())
c = int(input())

d = list(b)

count = 0
for score in d:
    if score == c:
        count += 1
print(count)
