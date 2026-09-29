#랜덤함수
# import random #파이썬에 있는 random 클래스 사용하겠다 선언

#첫번째입력숫자~두번째입력숫자까지 랜덤으로 정수값을 1개 넘겨줌.
#randint(1,100)
import random

random

# num= random.randint(1,100)
# print(num)

#1-5까지의 랜덤숫자를 출력하시오

num= random.randint(1,5)
input1 = int(input("1-5까지 범위의 숫자를 입력하세요>> "))
input2 = int(input("1-5까지 범위의 숫자를 입력하세요>> "))
print("랜덤숫자 :",num)
print("랜덤숫자: ",input1)
if (num==input1) or (num==input2) :
    print("당첨")
else:
    print("꽝")


#산술연산자 : +,-,*,/,//,%,**
#비교연산자: ==,!=,>,<,>=,<=
#논리연산자: and,or,xor

# 입력한 숫자가 2의 배수인지, 아닌지 출력하시오.
#a%2==0
# a= int(input("숫자입력 :"))
# if a%2==0 :
#     print("2의배수")
# else:
#     print("2의배수가 아님")
# print("입력숫자 :",a)





#입력한 숫자가 양수인지, 음수인지 출력하시오.
# 1.숫자입력 2.양수,음수 비교 3.출력

# a=int(input("숫자입력 : "))
# if a>0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")
# print("입력숫자:",a)
