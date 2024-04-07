# 예외처리
# try:
#     print("나누기 전용 계산기")
#     nums =[]
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     #if execpt nums.append(int(nums[0] / nums[1]))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], int(nums[2])))
# except ValueError:
#     print("나눌수 없는 숫자입니다.")
# # except ZeroDivisionError as err:
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except:
#     print("알 수 없는 오류 발생.")

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")