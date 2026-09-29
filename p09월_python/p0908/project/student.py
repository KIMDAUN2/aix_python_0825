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