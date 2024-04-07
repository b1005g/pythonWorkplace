A, B = map(int, input().split())
C = int(input())
B = B + C
d, m = divmod(B, 60)
A = A + d
B = m
d, m = divmod(A, 24)
A = m
print(int(A), int(B))