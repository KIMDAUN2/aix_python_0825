from 학생성적_py.연습.Func import *

readStu()
while True:
    choice = main_screen()
    if choice ==1:
        stu_input()
    elif choice ==2:
        stu_output()
    elif choice ==3:
        print("[학생성적수정]")
        stu_update()
        pass
    elif choice==8:
        print("[등수처리]")
    elif choice==9:
        writeStu()
    else:
        print("[프로그램 종료]")
        break