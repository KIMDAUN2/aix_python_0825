#리스트
# f=["사과","복숭아","수박","딸기"]
# if "참외" in f :
#     print("참외있다")
# else:
#     print("참외없다")

#리스트개수
# a=[1,2,3,4,5,6]
# print(len(a))

#원하는값 in 리스트, 원하는값 not in 리스트
# a=[1,3,5,7,9]
# if 7 in a:
#     print("원하는 수가 있습니다")
# else:
#     print("없습니다.")

# if 9 not in a:
#     print("yes")
# else:
#     print("no")

#1-100까지 랜덤숫자 3개를 리스트에 추가 입력한 숫자 1개가 있는지를 확인해서 있으면 당첨, 없으면 꽝
# 랜덤숫자 리스트 출력 ,입력숫자 출력

# import random
#sample은 중복숫자 안나옴
#range 는 첫번쨰적은 숫자 부터두번째적은 숫자 앞까지
# sc=random.sample(range(1,100),3)
# r=int(input("숫자입력"))
# if r in sc:
#     print("당첨")
# else:
#     print("꽝")
# print("랜덤숫자:",sc)
# print("입력숫자:",r)