def solution(s):
    s = list(s)
    cnt = 0 
    for i in range(len(s)):
        cnt += s.index(s[i-1])
    answer = cnt
    return answer

s = "banana"
print(solution(s))
