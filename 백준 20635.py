N = input()
color = list(input())
R = color.count("R")   #R
B = color.count("B")   #B
cnt = 0
R_P = color.index("R") # A의 위치
B_P = color.index("B") # B의 위치
for i in range(1,len(color)+1):
    if  color[i] == "R":
        target = []
        if len(target) > 0 and color[i - 1] == color[i]:
            target[len(target) - 1] += 1
        else:
            target.append([i])
            cnt = len(target)
if max(R,B) is R:
    cnt += 1
elif max(R,B) is B:
    cnt += 1
print(cnt)

