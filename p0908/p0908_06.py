class Student:
    total= 0
    avg=0

    #함수는 내부안에 있는것을 우선순위로 찾고 전역변수를 찾는다.
    #생성자
    def __init__(self,no,name,kor,eng,math):
        self.no=no   #self를 넣어야 외부에있는 변수에 값을 넣어줌,외부에 없으면 새로 값을 만들어줌
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3
        #self.rank=0      s1,s2한번에 다 추가 하고싶을때에는 함수안에 넣는다

    #미리 출력값을 선언해서 전체출력을 리턴해서 보내준다
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

    #점수 변경되었을때 쓰는 합계와 평균 함수
    def cal_total(self):
        self.total=self.kor+self.eng+self.math
    def cal_avg(self):
        self.avg=self.total/3


#객채선언시 바로 값 입력
s1 =Student(1,"홍길동",90,90,100) 
s2= Student(2,"유관순",100,100,99)

#출력 : 참조변수명.변수명
print(s1.name)                #홍길동
#수정: 참조변수명.변수명 =수정값
s1.name="홍길자"               #홍길자
print(s1.name)
#추가 : 참소변수명.변수명: 없는 변수 입력시 추가
s1.rank =1
print(s1.rank)

#전체출력
print(s1)
print(s2)

#수정
s1.kor=10
s1.cal_total()
s2.cal_total()   #s1과 s2는 각자 자기값을 출력한다.
s1.cal_avg()
print(s1)


#캡슐화: 변수 앞에__(언더바2개)
#클래스 내부에서만 값을 수정가능하다.
#캡슐화시 값을 수정할 수 있도록, setter,getter를 만들어줌.(함수)
#slef.__no