N, M = map(int, input().split()) # 바구니 수(N) , M 공을 넣는 수
a = [0] * N
m_1 = 0
m_2 = 0
for i in range(N+1):
        a[i-1] = i
for i in range(M):
    i,j = map(int, input().split()) # i,j 
    m_1 = a[i-1] 
    m_2 = a[j-1]
    a[i-1] = m_2
    a[j-1] = m_1
    # pocket[j-1], pocket[i-1] = pocket[i - 1], pocket[j - 1] 형태로 가능
print(*a)