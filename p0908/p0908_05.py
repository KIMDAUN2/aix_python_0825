class Student:    

    def __init__(self,no,name,kor,eng,math):
        self.no = no
        self.name =name
        self.kor = kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t"

    def cal_total(self):
        self.total = self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg = self.total/3


#--------------------------
class students:  #리스트를 만들어 클래스선언을 해서 append(추가)한다.
    slist = []
    #생성자: 객채선언시 실행됨.
    def __init__(self,s):   #선언해서 리스트생성하고 값 넣어줌
        self.slist.append(s)
    #함수: 함수호출시 실행됨.
    def add(self,s):         #계속해서 추가
        self.slist.append(s)



#---------------------------
#Students 객채선언
stu = students(Student(1,"홍길동",100,100,99))
#Stydents 객체 함수호출
stu.add(Student(2,"유관순",90,90,91))

for ss in stu.slist:
    print(ss)


# s =Student(1,"홍길동",100,100,99)
# print(s)

# #점수수정을 하면, sum,avg도 함께 변경이 되어야 함.
# s.kor=50
# s.cal_total()
# s.cal_avg()
# print(s)




# while True:
#     no = input("번호 : ")
#     name = input("이름 : ")
#     kor = int(input("국어 : "))
#     eng= int(input("영어 : "))
#     math = int(input("수학 : "))
#     stuList.append(Student(no,name,kor,eng,math))

#     for s in stuList:
#         print("-"*50)
#         print(s)
#         print("-"*50)