class Student:
    #생성자
    def __init__(self,*agrs):
        if len (agrs) ==5:       # 학생성적입력에서 객체 넣기
            self.no=agrs[0]      # no
            self.name =agrs[1]   # name
            self.kor=agrs[2]     # kor
            self.eng=agrs[3]     # eng
            self.math=agrs[4]    # math
            self.total=self.kor+self.eng+self.math
            self.avg=self.total/3
            self.rank=0
        elif len(agrs) == 8:     # stu.txt 파일에서 객체에 넣기
            self.no=agrs[0]      # no
            self.name =agrs[1]   # name
            self.kor=agrs[2]     # kor
            self.eng=agrs[3]     # eng
            self.math=agrs[4]    # math
            self.total=agrs[5]   
            self.avg=agrs[6]    
            self.rank=agrs[7]    


    
    #문자열함수
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

    def s_total(self):
        self.total= self.kor+self.eng+self.math

    def s_avg(self):
        self.avg=self.total/3

    def s_str(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"