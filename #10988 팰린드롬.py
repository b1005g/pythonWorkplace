S = list(input())
count = 0
for i in range((len(S)//2)) :
    if S[i] == S[-i-1]:
       count += 1
    else :
        count += 0
if count == (len(S)//2):
   print(1)
else :
   print(0)

'''
더 쉽게쉽게
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)
'''