from random import *
numbers = 1
char = 1
#for i in range(10):
#    print(i+1)

#for i in range(10):
#    print("=" + str(i+1) + "=")

for i in range(10):
    print("*" * i)

for i in range(10):
    print("*" * (10- abs(i)))

for i in range(-9,10):
    print("*" * (10- abs(i)))

# 경우의 수 계산
for i in range(4):
    for j in range(4):
        print(i + j, end=" ")
    print()

for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        print(n1, n2)

for i in range(6):                               # 오
    for j in range(10):                          # 열
        print(i + j, end=" ")
    print()
   
# 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 구해야 한다면
for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n % 4 == 0:
            print(n1, n2)

# 어떤 주식의 가격은 매일 한 번 동전을 던져서 앞면이 나오면 전날 가격의 2배가 되고, 
# 뒷면이 나오면 전날 가격의 절반이 된다. 1일에 주식의 가격이 1,024원이었을 때, 4일 주식의 가격이 나올 수 있는 경우를 모두 구한다. 
# (힌트: for 반복문이 3개 중첩되어야 한다)


U = randrange(0,5)
for i in range(2):
    for j in range(2):    
        for c in range(2): 
            print(1024 * (i*j*c) , 1024 / (4-(i*j*c)))


for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            print(1024 * 2 ** (i + j + k))