## 1-100 사이 랜덤번호를 맞추는 프로그램을 구현하시오
# 랜덤번호보다 높은 수를 입력하면 낮은 숫자입력,높으면 높은숫자 입력
# 정답을 맞추면 
# 정답숫자 :
# 입력숫자 횟수:
# 입력한 숫자:


import random
r=random.randint(1,100)
my=[]
mynum=0
count=0
while True :
    mynum=int(input("숫자입력:"))
    my.append(mynum)
    count=count+1

    if mynum ==r:
        print("정답입니다.")
        break
    elif mynum> r:
        print("입력한 숫자가 더 큽니다. 작은수 입력:")
    else:
        print("입력한 숫자가 더 작습니다. 큰 수 입력:")

print("정답숫자:", r)
print("입력숫자횟수:",my)
print("입력숫자:",count)    