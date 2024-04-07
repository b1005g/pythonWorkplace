from operator import index


python = "Python is amazing"
print(python.lower()) ## 소문자 변환
print(python.upper()) ## 대문자 변환
print(python[0].isupper())  ## 대문자 참/거짓 판별
print(python.replace("Python", "Java")) ## 문자변환

index = python.index("n")
print(index)
index = python.index("n", index + 1) ## 2번째 n 찾는방법
print(index)

print(python.find("n")) ## 위치찾는 함수 2번째
print(python.find("Java")) ## 포함되지 않는 경우 -1 반환
## index = python.index("엄") ## 포함되지 않는 경우 에러뜸
print(python.count("n")) ## n이 몇번 등장하는지

# 문자열 포맷

# method 1
print("a" + "b")
print("a", "b")
print("나는 %d살입니다" %20)
print("나는 %s을 좋아한다이기야" % "노무현")
print("Apple 은 %c로 시작해요." % "A")
# %s는 아무거나 출력가능

print("나는 %s살입니다." % 20)
print("나는 %s은 좋아하고 %s은 싫어합니다." % ("노무현", "윤석열"))

# method 2
print("나는 {}살입니다.".format(20))
print("나는 {}은 좋아하고 {}은 싫어합니다.".format("노무현", "윤석열"))
print("나는 {0}은 좋아하고 {1}은 싫어합니다.".format("노무현", "윤석열"))
print("나는 {1}은 좋아하고 {0}은 싫어합니다.".format("이재명", "윤석열"))

# method 3
print("나는 {age}살이고, {color}색을 좋아한다.".format(age = 20, color = "빨강"))

# method 4
age = 20
color = "빨강"
print(f"나는 {age}살이고, {color}색을 좋아한다.")