sentense = '나는 소년입니다'
sentense2 = " 파이썬은 존나쉽다"
print(sentense)
print(sentense2)
sentense3 = """
나는 소년 이고,
파이썬은 존나쉽다 """
print(sentense3)

# slicing
jumin = "990120-1234567" # 생년월일 + 성별, 지역번호 5, 검증번호 1
print("성별 : " + jumin[7]) # jumin is index[0]~index[14]
print("연도 : " + jumin[0:2]) # 0 ~ 2직전
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6]) # or jumin[:6]
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:]) # 맨 뒤에서 7번째 끝까지
print("뒤 7자리 : " + jumin[-1:]) # 맨 뒤에서 7번째 끝까지

#문자열처리
python = "Python is Amazing"
print(python.lower()) #소문자 변환
print(python.upper()) #대문자 변환
print(python[0].isupper()) #대문자이냐? 확인구문
print(len(python)) #문자 길이 반환
print(python.replace("Python" , "Java"))

index = python.index("n")
print(index) # " "에 들어가있는 문자가 몇번째에 있는지 확인가능
index = python.index("n", index + 1)
print(index)
print(python.find("Java")) # find -> 원하는 값 없으면 -1 반환, print(python.index("Java"))시는 오류
print(python.count("n")) #계산

name = "고봉균"
age = 35
print("엄준식 " + name + " Let`s go")
print("엄준식 " + str(age) + "살이다.") # str or , age ,