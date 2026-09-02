#로또맞추기 프로그램을 구현하시오.

import random

lotto =random.sample(range(1,46),6)
print("로또번호 확인:",lotto)
my=[]
for i in range(6):
    a=int(input("숫자입력:"))
    my.append(a)

count =0
answer=[]
for i in my:
    if i in lotto:
        count=count+1
        answer.append(i)

print("정답번호:",answer)
print("로또번호:",lotto)
print("입력번호:", my)
print("정답개수:", count)