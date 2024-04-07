# 승객별 운행시간 5~50 / 5~15분만 매칭시키기
from random import *
# passengers = range(1,51)
# passengers = list(passengers)
cnt = 0 # 탑승여부
for passengers in range(1,51) :
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(passengers, time))
        cnt += 1
    else: 
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(passengers, time))
        
print("총 탑승객 수 :{0}".format(cnt))