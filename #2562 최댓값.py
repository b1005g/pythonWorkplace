c =[]
for i in range(9):
    A = list(map(int, input().split()))
    c += A

print(max(c))
print(c.index(max(c))+1)
