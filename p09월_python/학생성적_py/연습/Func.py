from 학생성적_py.연습.student import Student
from 학생성적_py.연습.students import Students

stus=Students()
stuNun=1

def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8")as f:
        while True:
            str = f.readline()
            if str == "":break
            stu=str.split(",")
            for i,s in enumerate(stu):
                if 0<=i<=1:continue
                elif 2<=i<=5:stu[i] = int(s.strip())
