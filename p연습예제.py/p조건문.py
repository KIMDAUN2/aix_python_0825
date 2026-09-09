# #a,b를 입력받아 합계가 100 넘으면 100큼수, 100작은수 출력
# #입력
# a=int(input("숫자입력>>"))
# b=int(input("숫자입력>>"))
# #합계
# total=a+b
# #조건문
# if a+b >100:
#     print("100보다 큰 수")
# else:
#     print("100보다 작은수")



#입력한숫자가 양수인지 음수인지 출력
# a=int(input("숫자입력>>"))
# if a>0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")



#입력한숫자가 배수인지 출력
# a=int(input("숫자입력:"))
# if a%2==0:
#     print("배수입니다.")
# else:
#     print("배수가 아닙니다.")



#랜덤숫자
#랜덤숫자 2개를 출력해서 둘중 하나라도 맞으면 당첨
# import random
# num=random.randint(1,50)
# input1=int(input("숫자입력>>"))
# input2=int(input("숫자입력>>"))
# print ("랜덤숫자:",num)
# print("랜덤숫자:",input1,input2)
# if (num==input1) or (num==input2):
#     print("당첨")
# else:
#     print("꽝")



#현재시간,format함수 사용해서 2026년08월27일06시28분12초 출력
# import datetime
# now=datetime.datetime.now()
# print("현재시간>",now)
# print("{}년{}월{}일{}시{}분{}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))



#현재월을 상반기,하반기로 출력
# import datetime
# now= datetime.datetime.now()
# month=now.month
# if month>=7:
#     print("상반기")
# else:
#     print("하반기")



