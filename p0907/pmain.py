#학생성적프로그램
from pfunc import *


readstu()
while True:
    choice=main_screen()   #메인함수
    
    if choice == 1:
        stu_input()  #입력함수

    elif choice==2:
        stu_output()  #출력함수
    elif choice==3:
        pass
    elif choice==9:  #저장
        writestu()
    else:
        print("프로그램 종료")
        break






