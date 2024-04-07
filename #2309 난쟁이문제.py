c = []
S = 0 # 합
n =  0 # 난쟁이의 수
ans = []

for i in range(9):
    A = list(map(int, input().split()))
    c += A
c.sort()
for i in range(9):
    S += c[i]
    if S == 100:
        n = i-1
        break
    elif S != 100:
        if i > 7 :
            c.remove(c[i-1])
            S -= c[i-1]
            n = i-1
        else : continue
    elif S > 100 :
        while(1):
            S -= c[i-1]
            if S == 100:
                break
    else: continue
if S == 100:
    ans += c[:n+1] 
for i in range(8):
    print(ans[i])

# --------------------------------------
tall = []

for tc in range(9):
    N = int(input())
    tall.append(N)

total = sum(tall)
two_tall_sum = (total - 100)

out = []

for i in range(9):
    for j in range(i+1, 9):
        if tall[i] + tall[j] == two_tall_sum:
            out.append(tall[i])
            out.append(tall[j])

tall.sort()
for k in tall:
    if k not in out:
        print(k)
# https://ji-gwang.tistory.com/244
        
array = []
for i in range(9):
    array.append(int(input()))

array.sort()

sum_ = sum(array)

# 만약 모두다 더하고 2명을 뺐을 때 그 값이 100이라면 2개를 뺀 나머지 값들 출력
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if sum_ - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()