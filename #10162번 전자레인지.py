# 10162번 
T = int(input())

A = int(T/300)
B = int(T%300/60)
C = int(T%300%60/10) 
if int(T%300%60%10) != 0:
    print(-1)
else: print(A, B, C)