#QUIZ 사이트별 비밀번호 설정
# 규칙 : http:// 삭제
# 처음만나는점. 제외
# http://naver.com

input = "http://naver.com"
input = input[7:] 
print(input)
input3 = input.replace("http://" , "")
print(input3)
input2 = input[:-4]
print(input2)
input3 = input3[:input3.index(".")]
print(input3)
password = input2[0:3] + str(len(input2)) + str(input2.count("e")) + "!"
print(password)
print("{0}의 비밀번호는 {1}입니다.".format(input , password))

input = "http://google.com"
input = input[7:] 
input2 = input[:-4]
password = input2[0:3] + str(len(input2)) + str(input2.count("e")) + "!" #주의사항 : str() 개시발놈
print(password)
print("{0}의 비밀번호는 {1}입니다.".format(input , password))

