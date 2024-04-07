#2720번 동혁이 십년
# Q = 0.25 , D = 0.1, N=0.05, P= 0.01
Q = 0.25
D = 0.1
N = 0.05
P = 0.01
list = [Q,D,N,P]
list.reverse()

T = int(input())
C = int(input())
for i in list:
    result = C / list[i]
    C += C / list[i]
    if C % list == 0:
        break
print( Q, D, N, P)


# T = int(input())
# for i in range(T):
#     C = int(input())
#     q = C/25
#     d = C%25/10
#     n = C%25%10/5
#     p = C%25%10%5
#     print(q, d, n, p)