import random
def main_print():
        print("1.구구단 출력프로그램")
        print("2.1-10까지 숫자맞추기 프로그램")
        print("3.두 수를 입력받아 =,-,*,/ 결과값 출력프로그램")
        choice= int(input("원하는 번호 입니다."))
        return choice

def number_func():
        ran= random.randint(1,10)
        no=0
        my=[]
        while True:
            no=int(input("1-10사이 번호:"))
            my.append(no)
            if no == ran:
                print("정답입니다.")
                break
            elif no > ran:
                print(no,"보다 작은수 입니다.")
            else:
                print(no,"보다 큰 수 입니다.") 

def gugudan_func():
        for i in range(2,10):
            for j in range(1,10):
                print("{}x{}={}".format(i,j,i*j))
                #print(f"{i}x{j}={i*j}")
def cal_func():
        num1=int(input("숫자를 입력하시오."))
        num2=int(input("숫자를 입력하시오."))
        print("더하기 : ",num1+num2)
        print("빼기 : ",num1-num2)
        print("곱하기 : ",num1*num2)
        print("나누기 : ",num1/num2)




while True:
    choice = main_print()
    if choice==1:
        number_func()
    elif choice==2:
        gugudan_func()
    elif choice ==3:
        cal_func()
    else:
        print("잘못입력하셨습니다.")