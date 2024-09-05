# 11047
N,K = map(int, input().split())
A = []
count = 0
for i in range(1,N+1):
    A.append(input())

A.reverse()
for i in range(1,len(A)+1):
    count += int(K / int(A[i-1]))
    K %= int(A[i-1])
    if K % int(A[i-1]) == 0:
        break
print(count)