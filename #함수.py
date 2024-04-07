#함수
# def open_account():
#     print("새로운 계좌가 생성되었음.")

# open_account()

# def deposit(balance,money):
#     print("입금완료. 잔액은 {0}입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money :
#         print("출금완료. 잔액은 {0}입니다.".format(balance - money))
#         return balance - money
#     else: print("잔액이 부족합니다. 잔액은 {0}입니다.".format(balance))

# def withdraw_night(balance, money):
#     commision = 100
#     return commision, balance - money - commision

# balance = 0
# balance = deposit(balance , 1000)
# # balance = withdraw(balance, 500)
# commision, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}입니다.".format(commision, balance))

# def profile(name, age, main_lang):
#     print("이름은 {0}이며, 나이는{1}이고, 주 언어는{2}입니다."\
#           .format(name,age,main_lang))
# profile("엄준식", 20, "python")
# profile("김찬호", 25, "java")
# def profile(name, age = 17, main_lang="파이썬"):
#     print("이름은 {0}이며,\t나이는 {1}이고,\t주 언어는 {2}입니다."\
#            .format(name,age,main_lang))
# profile("이재석")
# profile("김형섭")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "엄준식", age = 25, main_lang="Python")
# profile(main_lang="Java", name = "최인석", age = 26, )

#가변인자를 이용한 함수호출

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0},\t나이 : {1}\t".format(name,age), end =" ")
#     print(lang1, lang2, lang3, lang4, lang5)
# profile("엄준식", 20, "Python", "C", "java", 'javascript', 'C++')
# profile("손인욱", 25, "Kotlin", "Swift", "", '', '')

# def profile(name, age, *langauge):
#     print("이름 : {0},\t나이 : {1}\t".format(name,age), end ="")
#     for lang in langauge:
#         print(lang, end = "")
#     print()

# profile("엄준식", 20, "Python", "C", "java", 'javascript', 'C++', "C#")
# profile("손인욱", 25, "Kotlin", "Swift")

# gun = 10 #전역변수
# def checkpoint(soldiers):
#     global gun                      #전역 공간에 있는 변수를 사용
#     gun = gun - soldiers            # gun은 함수 내에서 변수이므로 지역변수
#     print("함수 내 에서는 남은 총이 :{0}".format(gun))
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("함수 내 에서는 남은 총이 :{0}".format(gun))
#     return gun           
    
# print("전체 총 수 :{0}".format(gun))    
# gun = checkpoint_ret(gun,2)
# print("남은 총 수 :{0}".format(gun)) 

# 남자 = 키 x 키 x 22
# 여자 = 키 x 키 x 21
# 함수명 : std_weight, 키 = height, 성별 gender
# 표준체중은 소수점 둘째자리까지 표시

# gender = int(input())
# height = int(input())
# def std_weight(height, gender):
#     global weight 
#     if    gender == 1:
#           weight = (height/100) * (height/100) * 22
#           print(weight)
#     elif  gender == 2: 
#           weight = (height/100) * (height/100) * 21
#           print(weight)
# std_weight(175,1)
# print(weight)

# def std_weight_2(height, gender):
#      if gender == "남자":
#         return height * height * 22
#      else: 
#         return height * height * 21
# height = 175
# gender = "남자"
# weight2 = std_weight_2(height/100, gender)
# round 함수 round(함수, 2(자리수))
