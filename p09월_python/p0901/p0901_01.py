#반복문 for-반복/회수지정, while-조건

#####구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))



#####1-100 사이의 숫자 맞추기
#1.랜덤번호 1개 생성
import random
ran_no = random.randint(1,100)
#2.무한으로 입력받기
in_no = 0  #입력변수만들기
in_arr = []   #입력한 숫자 리스트저장
while True:
#3.숫자입력받기
    in_no=int(input("1-100사이 숫자입력 : "))
    #입력한 숫자를 리스트에 넣기
    in_arr.append(in_no)
#4.랜덤번호와 숫자비교
    if in_no ==ran_no:
        print("정답입니다.")
        break
    elif in_no > ran_no:     #입력한수가 크면
        print(in_no,"보다 작은수를 입력하세요.")
    else:
        print(in_no,"보다 큰수를 입력하세요.")
#5.결과출력(print)
print("입력한 모든 리스트: ", in_arr)
print("정답 : ",in_arr[-1])




