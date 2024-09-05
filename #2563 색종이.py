#2563 색종이
# 예제 (3,7), (15,7), (5,2) 겹치는 영역의 넓이에다가 나머지 2개
# 내 처음 생각은 겹치는 부분에서 가장 큰 x값 구하고, y값 구해서 곱해주는 형식으로하면?
# 200(N-1) + (15-3)(7-2)로 하면 260이 나와서. 즉 겹치는 부분만 구해서 하면 될줄 알았음.

N = int(input())
area = [[0] * 100 for _ in range(100)]
for i in range(N):
    y1, x1 = map(int, input().split())
    for i in range(x1, x1 +10):
        for j in range(y1, y1+10):
            area[i][j] = 1
result = 0
for _ in range(100):
    result += area[_].count(1)
print(result)