from random import *
a= 1+2
i= 0
# print(a)
# print(random())
# print(int(random() * 10) + 1) # 1~10 사이 미만 숫자

#for i in range(6):
#    print((int(random() * 45) + 1 ))
# print(randrange(1,45))
# print(randint(1,45))
# for i in range(a) -> for 변수 in range (반복횟수)   randrange(a,b) is repeat within a to b(but b is excluded)
# randint functuon is  1 ~ 45 integer

# Example 1) 월 4회 스터디, 3번 온라인 1번 오프라인 1~3 제외, 월별 28일
A = randrange(4,29)
B = randrange(4,29)
C = randrange(4,29)
D = randrange(4,29)

print("온라인 스터디 날짜는 매 월 매", A ,"일로 정해졌습니다.") # or print("온라인 스터디 날짜는 매 월 매" + str(A) + "일로 정해졌습니다.")
print("온라인 스터디 날짜는 매 월 매", B ,"일로 정해졌습니다.")
print("온라인 스터디 날짜는 매 월 매", C ,"일로 정해졌습니다.")
print("오프라인 스터디 날짜는 매 월 매", D ,"일로 정해졌습니다.") # list로 분배 필요 