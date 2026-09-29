#날짜함수
import datetime
import random


#리스트변경
a =[1,2,3,4,5]
print(a)
a[2]=30
a[3]=500
print(a)

#리스트삭제
a.pop[2]
print(a)
#리스트추가
a.append(200)
print(a)




#1~45 까지 랜덤 5개를 가져와서
#입력한 숫자가 있으면 당첨,없으면 꽝

# lotto=random.sample(range(1,46),5)
# print(lotto)
# iarr=[]
# #반복문
# for i in range(5):
#     iarr.append(int(input("숫자입력:")))

# #
# for i in range(5):
#     if iarr[i] in lotto:print("당첨")
#     else: print("꽝")


#랜덤5개
#randint-랜덤1개,sample-랜덤 여러개(중복불가),
#shuffle- 전체섞음, chiices-랜덤여러개(중복가능)
# a=random.randint(1,45)  #랜덤1개
# arr= random.sample(range(1,46),5) #1~45까지 중복없이 5개를 가져옴.
# print(arr)
# arr2=random.sample([1,2,3],2)
# print(arr2)
# arr3=[1,2,3,4,5]       #리스트 전체를 랜덤으로 섞어줌.
# random.shuffle(arr3)
# print(arr3)
# arr4 = [1,2,3,4,5]
# arr5= random.choices(arr4,k=5)  #리스트 해당개수만큼 가져옴.중복가능
# print(arr5)



# 리스트생성방법
# alist1=[0,0,0,0,0]
# alist2 =[0]*5
# alist3=list(range(1,6))  #1,2,3,4,5 
# print(alist1)
# print(alist1)
# print(alist2)




# 시간
# now = datetime.datetime.now
#year,month,day,hour.minute,second
# print(now)
# print(now.year)
# print(now.month)

# 랜덤 계절 구하기 random
# r_num=random.randint(1,12)
# print("현재계절:",r_num)
# if 3<=r_num<=5:
#     print("봄")
# elif 6<=r_num<=8:
#     print("여름")
# elif 9<=r_num and r_num<=11:
#     print("가을")
# else:
#     print("겨울")

#now.month
#01월,02월