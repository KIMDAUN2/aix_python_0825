#1-100 숫자맞추기
#1.랜덤번호 생성
import random
ran = random.randint(1,100)
no=0
my=[]
while True:
    no=int(input("1-100사이 번호:"))
    my.append(no)
    if no == ran:
        print("정답입니다.")
        break
    elif no > ran:
        print(no,"보다 작은수 입니다.")
    else:
        print(no,"보다 큰 수 입니다.")
print("입력횟수",my)
print("정답",ran)
