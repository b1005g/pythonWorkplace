#서강근육맨 20300
# PT당 운동기구는 2번, 리스트에서 2개를 뽑아서 M보다 같거나 작으면 됨.
N = int(input())
T = map(int, input().split()) # N은 운동기구수, T는 운동기구당 근손실
T = list(T)
T.sort()
result = 0

M = []
if int(N) % 2 == 0 :
    for i in range(0, int(N / 2)) :
        M = T[i] + T[N-1-i] 
        result = max(M, result)
        
elif N % 2 != 0:
    result = max(T)
    T = T[:N-1]
    for i in range(0, int((N-1)/2)):
        M = T[i] + T[len(T)-1-i]
        result = max(M,result)
print(result)