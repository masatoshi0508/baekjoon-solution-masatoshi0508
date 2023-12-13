t_1, e_1, f_1 = map(int, input().split())
Max = (t_1*3+e_1*20+f_1*120)
t_2, e_2, f_2 = map(int, input().split())
Mel = (t_2*3+e_2*20+f_2*120)

if Max > Mel:
    print('Max')
elif Max == Mel:
    print('Draw')
else:
    print('Mel')

