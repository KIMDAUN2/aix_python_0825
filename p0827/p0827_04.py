import random
import datetime  #현재시간을 가져오는 클래스선언


#1-6월까지는 상반기
#7-12월까지는 하반기
#8월
#현재월을 datetime함수를 사용해서 검색한 다음
#상반기,하반기 출력

#날짜함수를 사용해서 월을 변수에 저장을 한 후
#비교
#출력

# now=datetime.datetime.now()
# month=now.month 
# if month>=7:
#      print("{}월 :하반기.".format(month))
# else:
#      print("상반기")


#

#현재시간
# now = datetime.datetime.now()
# print("전체시간:",now)          #전체시간
# print("년도:",now.year)        #년도
# print("월:",now.month)         #월
# print("일:",now.day)           #일
# print("시:",now.hour)          #시
# print("분:",now.minute)        #분
# print("초:",now.second)        #초

#2026년 08월 27일 11시 12분 10초
#format함수사용
#print("{}년{}월{}일{}시{}분{}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))


#123 -> 5자리 중 공백은 0으로 채우시오.
# print("{:05d}".format(123))


#조건문안에조건문넣기/ a값을 입력받아 50보다크고100보다 작은수있지 50보다크고100보다 큰수인지 아니면50보다 작은수인지
# a=int(input("숫자입력>>"))
# if a>50:
#     if a<100:
#         print("50보다크고 100보다 작다")
#     else:
#         print("50보다크고 100보다 크다")
# else:
#     print("50보다 작은수")


#조건문 여러개 90=a,80=b,70=c,그 밑에는d
# a=int(input("숫자입력>>"))
# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# else:
#     print("D")


#랜덤숫자
# import random
# #랜덤숫자가 음수인지 양수인지 0은 0이라고 출력
# # no1=random.randint(-5,5)
# # print("랜덤숫자:",no1)
# # if no1>0:
# #     print("양수입니다.")
# # elif no1==0:
# #     print("0입니다.")
# # else:
# #     print("음수입니다.")


# #60점 이상 합격 50-59 재시험 0-49 불합격
# sc=random.randint(0,100)
# print("랜덤숫자>>",sc)
# if sc>=60:
#     print("합격")
# elif 50<=sc<=59 :
#     print("재시험")
# else:
#     print("불합격")

#봄,여름,가을,겨울

# import datetime
# now=datetime.datetime.now()
# if 3<= now.month <=5:
#     print("봄")
# if 6<= now.month <=8:
#         print("여름")
# if 9<= now.month <= 11:
#       print("가을")
# if (12==now.month) or (1<=now.month<=2):
#       print("겨울")


