n = int(input())
s = input()

count = 0
for i in s:
    if i in ['a', 'i', 'u', 'e', 'o']:
        count += 1

print(count)

