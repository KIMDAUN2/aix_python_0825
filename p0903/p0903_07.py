import sys
print(sys.builtin_module_names)

import math
dir(math)
print(math.log(10))
print(math.sin(10))


print(math.floor(10.921))  #버림   10
print(math.ceil(10.921))   #올림   11
print(round(10.921))       #반올림  11(값,소수점자리 ex)10.921,1





# # from func import cal1,cal2,cal3
# from func import *
# cal1()
# cal2()
# cal3()


# import func
# func.cal1()
# func.cal2()
# func.cal3()

#가변매개변수로 합계를 구하시오.
# def func1(*num): #가변매개변수
#     sum = 0
#     for n in num:
#         sum+=n
#     return sum

# print(func1(1,2,3))
# print(func1(1,2))
# print(func1(10,20,30,40,50))


#매개변수와 가변매개변수를 합쳐서 30,550을 만드시오
# def func2(a,b,*num): #매개변수와 가변매개변수 써보기
#     sum=0
#     sum= a + b
#     for n in num:
#         sum += n

#     return sum

# print(func2(10,9,11))
# print(func2(100,150,250,50))






# def func1(a,b,c):  #c:매개변수,지역변수
#     print(a)
#     return a+10

# #실행시작위치
# c=30  #전역변수
# result =func1(10,2,c)
# print(result)






# def func():
#     global a      #전역변수에 선언되어 있는 링크를 가져옴
#     a=10 #지역변수
#     print("func1 a :",a)

#실행시작포인트
# a=20  #전역변수
# func()
# print("전역변수 : ",a)


#함수는 함수의 끝을 만나면 모든변수를 다 지워버린다.
#함수는 호출을 하지 않으면 실행하지 않는다.








# #지역변수- 지역내에 있는 변수만 찾을 수 있다
# def func1():
#     a=10 # 함수a  / 지역변수-지역내에 있는변수만 찾을 수 있다
#     print("func1 a:",a)

# #지역변수- 없는상태
# #다른 함수 건드릴 수 없음
# #지역변수안에 변수가 없으면 매개변수를 통해 리턴을 받아 전역변수에서 찾아야 한다.
# def func2():
#     print("func2 a:",a)

# a = 20 #함수 밖 a / 전역변수 

# #실행
# func1() #10
# func2()