# 1010 다리 놓기, 조합법
import itertools
T = int(input())
a = []
b = []
ans = []
for i in range(T):
    N,M = map(int, input().split())
    for i in range(M):
        a += ["M" * (i+1)]
    b += itertools.combinations(a,int(N))
    ans.append(len(b))
for i in range(T+1):
    print(ans[i-1])
    
#---------------------------------------------------------
def factorial(k):
    sum = 1
    for i in range(1, k + 1):
        sum *= i
    return sum


def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


t = int(input())
lst = []
for i in range(t):
    n, m = map(int, input().split())
    lst.append(nCr(m, n))

for i in lst:
    print(i)