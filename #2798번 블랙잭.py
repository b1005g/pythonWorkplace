#2798번 블랙잭
# 처음에는 이중 for문으로 i,j j+1로 시작해서 찾으려고했는데 자꾸 이상하게되서 바꿨습니다.
N, M = map(int, input().split())
Card = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if Card[i] + Card[j] + Card[k] > M :
                continue
            else :
                reslut = max(result, Card[i] + Card[j] + Card[k])
print(reslut)
'''
from itertools import combinations
N, M = map(int,input().split())
nums = list(map(int,input().split()))
result=0
for cards in combinations(nums,3):
    if sum(cards) <= M:
        result = max(result,sum(cards))
print(result)
'''