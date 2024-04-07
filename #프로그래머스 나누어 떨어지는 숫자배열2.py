#코드프로그래머스
def solution(arr, divisor): 
    answer = []
    for i in range(len(arr)):
        b = arr[i-1] % divisor
        if b == 0:
            answer.append(arr[i-1])
        elif b > 0 :
            answer += []
    if answer == [] :
        answer = [-1]
    answer.sort()
    return answer

array = [3,2,6]
print(solution(array, 10))

