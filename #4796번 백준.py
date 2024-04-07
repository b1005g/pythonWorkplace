#4796번 백준


vacation = 0
while True:
    L,P,V =map(int, input().split())
    C = V // P
    vacation += C * L 
    V -= C * L
    print(vacation)
    if V // P == 0  :
        vacation += V % P
        print(vacation)
        break
    elif V % P > L :
        vacation += V % P - L
        print(vacation)
        break
    if (L, P, V) == (0, 0, 0):
        break 
    break
print(vacation)

        
i = 1
while(1):
    l,p,v = map(int,input().split())

    if p == 0 and l == 0 and v == 0:
        break

    answer = (v//p)*l + min((v%p),l)
    print('Case {0}: {1}'.format(i, answer))
    i += 1