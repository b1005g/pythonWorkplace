subway1 = 10
subway2 = 20
subway3 = 30
subway =[10,20,30]
print(subway)
print(subway.index(20))
# 추가
subway.append(40)
print(subway)
# 배열 사이에 넣기
subway.insert(1,15)
print(subway)
# 뒤에서부터 추첨
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
# 계산
subway.append(10)
print(subway)
print(subway.count(10))

# 정렬
num =[5,2,4,3,1]
num.sort()
print(num)

#뒤집기
num.reverse()
print(num)

#지우기
num.clear()
print(num)

# list는 자료형에 구애받지않고 섞어서 쓸수있음
num =[5,2,4,3,1]
mix =["엄준식", True, 20]
num.extend(mix)
print(num)

# 중복 x , 사전 (key , value)
cabinet = {3: "엄준식" , 100: "김형섭"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
print(cabinet[5]) # error, program end
print("hi")
print(cabinet.get(5)) # -> none
print(cabinet.get(5, "사용가능")) # none 대신 사용가능이라는 문자 출력.
print(3 in cabinet) # boolean 판단.
print(5 in cabinet)

cabinet = {"A-3": "엄준식" , "B-100": "김형섭"}
print(cabinet)
cabinet["A-3"] = "이재석"
cabinet["C-20"] = "김찬호"
print(cabinet)
del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)

#튜플, 속도 리스트보다 빠름. 변경되지않는 목록 사용시 사용 , add 제공 x
menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

name = "엄준식"
age = 20
hobby = "coding"
print(name, age, hobby)
(name, age, hobby) = ("엄준식" ,20 ,"coding")
print(name, age, hobby)

# 세트(집합) , 중복x , 순서x
my_set = {1,2,2,3,3}
print(my_set)

java = {"이재석" , "엄준식" , "김찬호"}
python = set(["이재석", "김형섭"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합(java는 가능, python은 불가능)
print(java - python)
print(java.difference(python))

#add element
python.add("김찬호")
print(python)
#minous element
java.remove("김찬호")
print(java)

steamer = {"이재석", "엄준식", "김찬호"} # set
print(steamer, type(steamer))
steamer = list(steamer)
print(steamer)
steamer = tuple(steamer)
print(steamer)
steamer = set(steamer)
print(steamer)


