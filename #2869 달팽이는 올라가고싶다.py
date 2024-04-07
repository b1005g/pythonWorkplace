A,B,V = map(int, input().split())
d = 0 # 걸리는 날짜 
if A - B == 1:
    d = V - A + (A - B)
else : d = (V - A) + B
print(d)


import math
a , b , v = map(int,input().split())
one_day = (a - b)
semi_one_day = (v - a)
day = (semi_one_day/one_day)
if (a >= v):
    print(1)
else:
    if (day == float(day) and float(day) > 1):
        print(math.ceil(day)+1)
    elif (day == int(day) and int(day) > 1):
        print(day+1)
    else:
        print(math.ceil(day)+1)