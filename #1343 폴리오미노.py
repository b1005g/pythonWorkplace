#1343 폴리오미노
# AAAA, BB
x = input()
cnt = 0
ans = []

for i in range(len(x)+1):     #search
    if x[i-1] == '.':
        ans.append('.')
        print(ans)
    elif cnt / 4 == 1 :
            ans.append("AAAA")
            cnt -= 4
            print(ans)
    elif cnt == 2:
            ans.append("BB")
            cnt -= 2
            print(ans)
    else : cnt += 1
    print(cnt)
print(ans)    


# import sys

# board = sys.stdin.readline().rstrip()
# result = []

# while board:
#     if board[0] == '.':
#         result.append('.')
#         board = board[1:]
#         continue
    
#     else:
#         i = 0
#         count = 0
#         while i < len(board) and board[i] != '.':
#             i += 1
#             count += 1

#         board = board[count:]

#         while count > 0:
#             if count >= 4:
#                 result.append('AAAA')
#                 count -= 4
            
#             elif count >= 2:
#                 result.append('BB')
#                 count -= 2
            
#             else:
#                 break
        
#         if count != 0:
#             result = ['-1']
#             break

# print(''.join(result))

    #     if "X" in X[i:i+3] :
    #         x.count("X")
    
    #     print(" ")

    # elif : X = x.count("X")
    #     if x.count("X") == 4:
    #         result = x.count("X")
    #         print(x.replace("X", "A"))
    #     elif x.count("X") == 2 :
    #         print(x.replace("X","B"))
    
        
        
    

