class Student:  #객채선언 앞글자는 대문자
    #생성자(변수가 있으면 있는자리에 넣어주고, 변수가 없으면 만들어서 준다)
    def __init__(self,no,name,kor,eng,math):
        self.__no= no
        self.__name = name
        self.__kor=kor            #캡슐화: 클래스내부에서만 값을 수정(언더바2번)
        self.__eng=eng
        self.__math=math
        self.__total=kor+eng
        self.__avg= (kor+eng+math)/3

    #특수(참조변수 사용)
    def __str__(self):
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"

    #값 가져오기
    def get_kor(self): 
        return self.__kor
    #값을 바꾸기
    def set_kor(self,kor):  #캡술화를 하면, 잘못된 값이 입력될떼 에러처리
        if kor<0:
            print("잘못된 값이 들어옴.")
            return
        self.__kor = kor

    #클래스 내 함수 매개변수 첫번째 self
    def total(self):
        self.__total = self.__kor+self.__eng+self.__math

    def avg(self):
        self.__avg = self.__total/3

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.__total,f"{self.__avg:.2f}",sep="\t")

stuList=[]
#객채선언,참조변수
s =Student(1,"홍길동",100,100,99)
print("-"*50)
print(s)
print("-"*50)
s.kor = 70  #클래스 변수값 수정- 있는변수에 값을 넣으면 수정     #함수내에서 캡슐화로 인해 수정 안됌
s.math = 100  #클래스 변수 추가- 없는 변수 값을 넣으면 추가
s.set_kor(50)  #캡술화로 인해 수정되지 못하는 것을 다시 수정 가능하게 하는것  #setter,getter를 사용해서 수정,확인해야함
s.total()
s.avg()
s.print()
print(s)