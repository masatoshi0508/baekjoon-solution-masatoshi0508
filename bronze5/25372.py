n = int(input())

for _ in range(n):
    s = input() #s = secret number
    if 6 <= len(s) <= 9:
        print('yes')
    else:
        print('no')

# n = int(input())

# for _ in range(n):
#     s = input() #s = secret number
#     if len(s) >= 6 and len(s) <= 9:
#         print('yes')
#     else:
#         print('no')