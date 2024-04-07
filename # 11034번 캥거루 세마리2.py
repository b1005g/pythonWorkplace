# 11034번 캥거루 세마리2
# 사이에 있는 수만큼 이동가능
while(1):
    try:
        A,B,C = map(int, input().split())
        m = max(B-A ,C-B)
        print(m-1)
    except:
        exit()