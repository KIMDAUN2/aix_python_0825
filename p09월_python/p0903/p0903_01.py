#c,자바: 컴파일러 언어- 모든소스를 기계어로 번역 후 프로그램진행
#파이썬: 스크립트 언어 -  한 줄 씩 기계어로 번역 후 프로그램진행
#def: 함수선언
#호출(print)하는 곳에서부터 실헹
#힘수사용이유:코드재사용, 코드 간결
#주는 것은 매개변수, 받는것은 return

def d_print():
    for i in range(1,11):
        print(i)

def hello_print():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

#------------
d_print()
hello_print()


def cal(n1,n2):
    r1=n1+n2
    r2=n1-n2
    r3=n1*n2
    r4=n1/n2
    return r1,r2,r3,r4

n1= int(input("숫자입력:"))
n2= int(input("숫자입력:"))
r1,r2,r3,r4=cal(n1,n2)
print(r1,r2,r3,r4)