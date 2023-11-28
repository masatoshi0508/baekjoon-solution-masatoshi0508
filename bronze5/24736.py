T, F, S, P, C = map(int, input().split())
T1, F1, S1, P1, C1 = map(int, input().split())

print(T*6+F*3+S*2+P*1+C*2, T1*6+F1*3+S1*2+P1*1+C1*2)

# for _ in range(2):
#     score = 0
#     T, F, S, P, C = map(int, input().split())
#     score = T*6 + F*3 + S*2 + P*1 + C*2
#     print(score, end=" ")