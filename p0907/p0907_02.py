#(다른폴더의 함수 가져와 사용하기)
# def함수를 ctrl+x 후 func.py 폴더 만들어서 ctrl+v후 아래 3가지쓰기

#import func         /func
#import func as fn   /fn
from func import hap,hap2,hap3



#1. 두 수를 입력받아, 두 수의 합을 구하시오.
# 매개변수x,return x
hap()
print("hap()완료")

#2. 두 수를 입력받아, 두 수의 합을 구하시오.
# 매개변수o,return x
num1=int(input("1숫자입력:"))
num2=int(input("2숫자입력:"))
hap2(num1,num2)
print("hap2()완료")

#3. 두 수를 입력받아, 두 수의 합을 구하시오.
# 매개변수o,return o
num1=int(input("1숫자입력:"))
num2=int(input("2숫자입력:"))
sum=hap3(num1,num2)
print(sum)
print("hap3()완료")