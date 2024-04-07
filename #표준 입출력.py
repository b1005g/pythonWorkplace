#표준 입출력
import sys
print ("Python", "Java", sep =",") # sep = , 부분에 어떤걸 넣을것인지
print ("Python", "Java", "Javascript", sep =" vs ")
print ("Python", "Java", "Javascript", sep =" vs ", end = "?")
print ("어떤것이 점유율이 높은지", end  = "?")

print ("Python", "Java", file  = sys.stdout)
print ("Python", "Java", file  = sys.stderr)


scores = {"math":0, "english":50, "coding":100}
for subject, score in scores.items(): #key, values를 튜플로
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

은행 대기순번표
001, 002, 003, ...
for number in range(1,21):
    print("대기번호 : " + str(number).zfill(3)) #3개 크기만큼 공간을 차지하고 빈공간을 0

answer = input("아무값이나 입력하세요 : ") # str로 저장.
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

# 다양한 출력포맷
print("{0: >10}".format(500))
print("{0: >10}".format(-500))

#양수일때는 + / 음수일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬 후 빈칸을 _
print("{0:_<+10}".format(500))

#3자리마다 ,찍어주기
print("{0:,}".format(1000000))

#3자리마다 ,찍어주기(부호포함)
print("{0:+,}".format(1000000))

#3자리마다 ,찍어주기(부호포함, 자릿수 확보) 빈자리는 ^ 
print("{0:^<+30,}".format(1000000000000))

#소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) #3번째 자리에서 반올림

###파일 입출력
scorefile = open("score.txt", "w", encoding="utf8") # w = write
print("수학 : 0", file = scorefile)
print("영어 : 50", file = scorefile)
scorefile.close()

score_file = open("score.txt", "a", encoding="utf8") # a = 덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 이동, 커서는 다음줄로 읻옹
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()    

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()


####### pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "엄준식", "나이":24, "취미":["게임","야구","축구"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 변수에 불러오기
print(profile)
profile_file.close()


### with
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


## with문으로 파일업로드하고 불러오기

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("엄준식은 살아있다.")

with open("study.txt", "r", encoding="utf8") as study_file:
     print(study_file.read())
