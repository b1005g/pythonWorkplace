# 11021 A+B -7
import sys
T = int(sys.stdin.readline())
result = []
for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    result.append(A+B)

for i in range(T):
    print("Case #",i+1,": ", result[i], sep ='')