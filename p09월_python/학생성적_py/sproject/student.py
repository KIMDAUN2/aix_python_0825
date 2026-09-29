class Student:
    
    def __init__(self,no,name,kor,eng,math):              #만들때 필요한 정보 입력
        self.no=no
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

    def __str__(self):                                    #문자열로 바꿔 보여주는 방법
        return(f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}")

    def s_total(self):
        self.total= self.kor +self.eng +self.math

    def s_avg(self):
        self.avg=self.total/3
        



s1=Student(1,"홍길동",100,100,100)
s2=Student(2,"유관순",100,100,100)