# 프로그래머스 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    a = []
    b = []
    for i in range(len(strings)):
        a = strings[i-1]
        print(a[n])
        b.append(a[n])
    b.sort()
    print(a.index(b))
    # for i in range(len(strings)):
    #     c = a.index(b)
    #     answer.append(c)
    return answer
strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))


# for i in range(len(strings)): strings[n]