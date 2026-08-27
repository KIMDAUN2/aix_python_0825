#1-100까지 랜덤숫자 3개를 리스트에 추가
# 입력한 숫자 1개가 있는지를 확인해서
# 있으면 당첨, 없으면 꽝
# 랜덤숫자 리스트 출력
# 입력숫자 출력


import random
arr = random.sample(range(1,100),3)
input1=int(input("숫자입력 :"))
if input1 in arr:
    print("당첨")
else:
    print("꽝")

print("랜덤숫자 : ",arr)
print("입력숫자 :",input1)









#중복없이 1-100사이 숫자 추출
#arr2= random.sample(range(1,100),3)