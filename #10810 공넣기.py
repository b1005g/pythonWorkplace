N, M = map(int, input().split()) # 바구니 수(N) , M 공을 넣는 수
a = [0] * N 
for n in range(M):
    i,j,k = map(int, input().split()) # i,j 바구니의 번호 i~j k라고 써있는 공을 넣는다.
    for e in range(j-i+1) :
        a[i+e-1] = k
print(*a)