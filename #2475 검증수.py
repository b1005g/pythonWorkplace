T = map(int, input().split())
T = list(T)
b = 0
for i in range(len(T)) :
    a = T[i-1]
    b += a * a
print(b % 10)