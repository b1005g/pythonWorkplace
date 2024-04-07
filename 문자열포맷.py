# 문자열포맷
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬")
print("Apple이라는 단어는 %c로 시작해요" % "A")
print("나는 %s살입니다." % 20)
print("나는 %s와 %s를 좋아해요" %("A","B"))

# .format()함수를 이용한 format
print("나는 {}살입니다." .format(20))
print("나는 {1}와 {0}를 좋아해요".format("A" ,"B"))

print("나는 {age}살이며, {what}를 좋아해요".format(age=20, what ="A"))

# f-strings
age = 20
color = "빨간색"
print(f"나는 {age}살이며, {color}를 좋아해")

#탈출문자
print("백문이 불여일견 \n백견이 불여일타")

#\"
print("나는 '고봉균'입니다.")
print('나는 "고봉균"입니다.')
print("나는 \"고봉균\" 입니다.")

#\\
print("경로는 C:\\Users\\b1005\\OneDrive\\바탕 화면\\programming\\pythonWorkplace> 입니다.")

#\r : 커서를 맨앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스(한글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")



