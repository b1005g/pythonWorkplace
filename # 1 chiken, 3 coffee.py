# 1 chiken, 3 coffee
# 댓글 20, id 1~20(num) random shuffle, sample
from random import*
people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # range(1,21)
# print(people)
shuffle(people)
# print(people)
# print(sample(people,1))
# print(sample(people,3))
winners = sample(people,4)
chiken = sample(winners,1)
print("치킨 당첨자 :{0}".format(winners[0]))
print("커피 당첨자 :{0}".format(winners[1:]))