# 다른 폴더에 있을경우 : from import해야함
#from 폴더명 import 파일명
from project import students 
from project import student

stus = students.Students()
#stus.slist =[s1]
print(len(stus.slist))

s1 = student.Student(1,"홍길동",100,100,99)
stus.add(s1)
stus.add(student.Student(2,"유관순",90,90,91))

stus.print()
