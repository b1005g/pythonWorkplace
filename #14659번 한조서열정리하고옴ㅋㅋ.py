#14659번 한조서열정리하고옴ㅋㅋ
# 용들은 처음 출발한 봉우리보다 높은 봉우리를 만나면 그대로 공격을 포기하고 금강산자락에 드러누워 낮잠을 청한다고 한다. 
# 봉우리의 높이는 모두 다르고 모든 용들은 오른쪽으로만 나아가며, 중간에 방향을 틀거나, 봉우리가 무너지거나 솟아나는 경우는 없다.

N = int(input())
M = map(int,input().split())
M = list(M)
Kill = 0

for i in range(1, N-1):
    if int(M[i-1]) - int(M[i]) > 0: # Type error
        Kill += 1
        result = max(result, Kill)
    else: print(Kill)
# v-------------------------------------------------------------
    
N = int(input())
mountain = list(map(int, input().split()))

result = 0
count = 0
height = 0

for i in range(len(mountain)):
    if mountain[i] < height:
        count += 1
        result = max(result, count)
    else:
        height = mountain[i]
        result = max(result, count)
        count = 0

print(result)