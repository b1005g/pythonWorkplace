# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
N = int(input())
index = 1
for N in range(2,10):
    for index in range(1,10):
        print("{0} * {1} = {2}".format(N ,index, N * index))    

N = int(input())
index = 0
for i in range(1,10):
    index += 1
    print("{0} * {1} = {2}".format(N ,index, N * index)) 

#반복변수에 N 넣지말자. 
T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    print(A+B)

#range(T)하면 T까지됨ㅇㅇ;
    
#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.   
n = int(input())
print(int(n*(n+1)/2))

#준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.
#영수증에 적힌, 구매한 각 물건의 가격과 개수,구매한 물건들의 총 금액을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

#첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다. 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

X = int(input())
N = int(input())
cost = 0
for i in range(N):
    a,b = map(int, input().split())
    cost = cost + a * b

if cost == X:
     print("Yes")
else:print("No")