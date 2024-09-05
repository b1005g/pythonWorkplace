#2231 분해합
N = int(input())
e = N // 10
print(e)
arr = []
'''
for i in range(10):
    for j in range(10):
        for k in range(10):
            print()  
'''
'''
n = int(input())
result = 0
for i in range(1, n+1):
    nums = list(map(int, str(i))) # i를 문자열로 변환하여 각 자리의 숫자를 개별적으로 추출한 후, 이를 정수 리스트로 변환
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)​
'''
