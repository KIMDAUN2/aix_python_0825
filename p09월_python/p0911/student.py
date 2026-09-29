#학생 한명을 표현하기 위한 설계도
class Student:


    #생성자
    def __init__(self,*agrs):
        if len(agrs) == 5:
            self.no=agrs[0]
            self.name=agrs[1]
            self.kor=agrs[2]
            self.eng=agrs[3]
            self.math=agrs[4]
            self.total=self.kor+self.eng+self.math
            self.avg=self.total/3
            self.rank=0
        elif len(agrs)==8:
            self.no=agrs[0]
            self.name=agrs[1]
            self.kor=agrs[2]
            self.eng=agrs[3]
            self.math=agrs[4]
            self.total=agrs[5]
            self.avg=agrs[6]
            self.rank=agrs[7]

    #객체를 출력할때
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

    #성적 수정 후 변경되는 메서드함수
    def s_total(self):
        self.total= self.kor+self.eng+self.math

    def s_avg(self):
        self.avg=self.total/3

    def s_str(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"