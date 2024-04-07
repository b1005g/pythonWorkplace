#1193 분수찾기
# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 ->
# 행과 열에 따라서 분수저장 다름, (3,2) -> 3/2

X = int(input())
a = []
b = []
for i in range(X+1):
    if i % 2 == 0:
        for e in range(1,i+1):
            a.append(e) 
            b.append(i-(e-1))
    elif i % 2 !=0 :
        for e in range(1,i+1):
            a.append(i-(e-1)) 
            b.append(e)          
print(str(a[X-1])+ "/" + str(b[X-1]))


#----------------------------------------------------

num = int(input())
line = 1
max_num = 1
while num > max_num:
    line += 1
    max_num += line
gap = max_num - num

if line % 2 == 0:
    top = line - gap
    low = gap + 1
    
else:
    top = gap + 1
    low = line - gap
print(f'{top}/{low}')







# 1  2  6  7  15 16 28 29
# 3  5  8  14 17 27 30
# 4  9  13 18 26 31
# 10 12 19 25 32
# 11 20 24 33
# 21 23 34
# 22 35
# 36

# 2 <-> 3 
# 4 <-> 6 
# 7 <-> 10
# 11 <-> 15
# 16 <-> 21

# 1  6 15 28
# 2 7 16 29
# 5, 9, 13 --> 공차가 4씩 증가
