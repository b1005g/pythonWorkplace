# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

# i,j,k = map(int, input().split())

# if    i == j == k:
#       money = 10000 + (i)*1000
#       print(money)
# elif  i == j !=k or i != j == k or i == k != j : 
#       if i == j :
#         money = 1000 + i*100
#         print(money)
#       elif j == k :
#         money = 1000 + j*100
#         print(money)
#       elif i == k :
#         money = 1000 + k*100
#         print(money)    

# elif  i >> j and k :
#       money = i * 100
#       print(money)
# elif  j >> i and k :
#       money = j * 100
#       print(money)
# elif  k >> i and j :
#       money = j * 100
#       print(money)

a, b, c = map(int, input().split())

if a == b == c:
    money = 10000 + a*1000

elif a == b or a == c or b == c:
    if a == b or a == c:
        money = 1000 + a*100
    else: money = 1000 + b*100
else: money = max(a, b, c) * 100

print(money)
         
# max, min 함수 잘 활용하기.