# 2920 음계
T = map(int, input().split())
T = list(T)
a = [1, 2, 3, 4, 5, 6, 7, 8]
c = a[::-1]
if a == T :
    print("ascending")
elif c == T :
    print("descending")
else : print("mixed")
