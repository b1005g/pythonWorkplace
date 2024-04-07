customer = "엄준식"
index = 5
while index >=1 :
      print("{0} 손님 커피가 준비되었읍니다. {1}번 남았읍니다." .format(customer, index))
      index -= 1
      if index == 0:
         print("커피는 폐기처분되었읍니다.")

customer2 = "김찬호"
index = 1
while True :
      print("{0} 손님 커피가 준비되었읍니다. 호출 {1}회" .format(customer2, index))
      index += 1
      break
      
customer3 = "이재석"
person = "unknown"

while person != customer3 : 
      print("{0} 손님 커피가 준비되었읍니다." .format(customer3))
      person = input("이름이 어떻게되세요?")

# contiune / break
absent = [2,5]
no_book = [7]
for student in range (1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업없다. {0}은 교무실로 와라".format(student))
        break
    print("{0}, 책을 읽어라".format(student))

#한줄 for
student = [1,2,3,4,5]
print(student)
student =[i+100 for i in student]
print(student)

student2 = ["엄준식(아무무)","김찬호(랄로)","이재석"]
student2 =[len(i) for i in student2]
print(student2)

student3 = ["sexy","bitch","fuck"]
student3 =[i.upper() for i in student3]
print(student3)

