# 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성
king,queen,Rook,vishop,knight,pon = map(int, input().split())

if  king != 1:
    if   king > 1 :
         king = 1 - king
    elif king < 1 :
         king = 1 - king
if  king == 0 :
    king = 0

if  queen != 1:
    if   queen > 1 :
         queen = 1 - queen
    elif queen < 1 :
         queen = 1 - queen
elif queen == 1 :
     queen = 0    

if  Rook != 2:
    if   Rook > 2 :
         Rook = 2 - Rook
    elif Rook < 2 :
         Rook = 2 - Rook
elif Rook == 2 :
     Rook = 0    

if  vishop != 2:
    if   vishop > 2 :
         vishop = 2 - vishop
    elif vishop < 2 :
         vishop = 2 - vishop
elif vishop == 2 :
     vishop = 0   

if  knight != 2:
    if   knight > 2 :
         knight = 2 - knight
    elif knight < 2 :
         knight = 2 - knight
elif knight == 2 :
     knight = 0    

if  pon != 8:
    if   pon > 8 :
         pon = 8 - pon
    elif pon < 8 :
         pon = 8 - pon
elif pon == 8 :
     pon = 0
       
cnt = (king, queen, Rook, vishop, knight, pon)
print(cnt)

#################################################################################
k, q, l, b, n, p = map(int, input().split())

chess = [k, q, l, b, n, p]

chess_rull = [1, 1, 2, 2, 2, 8]

for i in range(len(chess)):

    chess[i] = chess_rull[i] - chess[i]

print(*chess)

# print([x-y for x,y in zip([1,1,2,2,2,8],map(int,input().split()))])
# zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

# (1, 'A')
# (2, 'B')
# (3, 'C')
    
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for i in range(3):
    pair = (numbers[i], letters[i])
    print(pair)

#(1, 'A')
#(2, 'B')
#(3, 'C')

#병렬처리
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)

#1 A a
#2 B b
#3 C c
#4 D d
#5 E e