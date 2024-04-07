# 5597번 과제 안내신분?
a = []
b = [1, ... , 30]
c =[]
for i in range(28):
    N = list(input().split())
    a += N
a.sort()
print(a)
for i in range(28):
    if a[i] != b[i]:
        c += [b.pop(i-1)]
        print(c)
        continue
    elif len(a) == len(b):
        break
print(*c)
# --------------------------------------------
import sys

A=[]
B=[]
n=0

for i in range(28):
    C=int(sys.stdin.readline())
    A.append(C)

for i in range(30):
    n+=1
    D=A.count(n)

    if D==0:
        B.append(n)
        B.sort()

    else:
        print(C)

print(B[0])
print(B[1])