#로또맞추기 예제
import random

#로또 랜덤부분
# lotto = random.sample(range(1,46),6)
# print("확인로또:",lotto)
#숫자 6개 입력
# myNum=[]
# for i in range(6):
#     no=int(input("숫자입력 :"))
#     myNum.append(no)

#맞는지 확인
# count = 0
# answer =[]
# for i in myNum :
#     if i in lotto:
#         count = count =1
#         answer.append(i)

#출력하기
# print("정답번호 :",answer)
# print("로또번호 :",lotto)
# print("입력번호 :",myNum)
# print("정답개수 :",count)

#########################################

# myNum = []
# i=
# while i<6:
#     no =int(input("숫자입력 :"))
#     if no not in myNum:
#         myNum.append(no)
#         i=i+1
#     else:
#         print("번호가 있습니다.")






# import random
#1개 랜덤
# a = random.randint(1,45)
# print(a)
#리스트를 섞어줌.
# alist=list(range(1,46))
# random.shuffle(alist)
# print(alist)
#랜덤으로 개수만큼 추출
# ranArr=random.sample(range(1,46),6)
# print(ranArr)
#랜덤으로 개수만큼 추출을 하는데 중복이 가능함
# ranArr2=random.choices(range(1,46),k=6)
# print(ranArr2)




#입력숫자 6개 저장

# myNum = []
# i=0
# while i<6:
#     no =int(input("숫자입력 :"))
#     if no not in myNum:
#         myNum.append(no)
#         i=i+1
#     else:
#         print("번호가 있습니다.")

# print("입력숫자:",myNum)



#for문은 else까지 출력에 포함하여  예를 들면 4번 중복되면 정답이 3개만 나온다
# for i in range(6):
#     no=int(input("숫자입력: "))
#     if no not in myNum:
#         myNum.append(no)
#     else:
#         print("번호가 있습니다.")