from p09월_python.p0911.student import Student      #다른 파일에 있는 것을 가져오는것
from p09월_python.p0911.students import Students

#객채선언하기
stus=Students()
stuNum= 1


#파일에서 학생 성적 읽어오기
def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str = f.readline()
            if str == "":break
            stu=str.split(",")

            for i,s in enumerate(stu): 
                if 0<=i<=1:
                    continue
                elif 2<=i<=5:stu[i] = int(s.strip())
                elif i==6:stu[i] = float(s.strip())
                elif i==7:stu[i] = int(s.strip())

            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            stuNum = len(stus.slist)+1


#학생데이터를 파일에 저장
def writeStu():
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:  #f는 열어놓은 파일을 가리키는 변수
        for s in stus.slist:                   #slist에 들어있는 stu를 꺼내보기
            str=s.s_str()                    #객체자체를 파일에 바로 저장하기 어려워 문자열 형태로 변환
            f.write(str+"\n")
        print("성적파일이 저장되었습니다.")
        print()


#메인화면 출력
def main_screen():
    print("[학생성적프로그램]")
    print("1.성적입력")
    print("2.성적출력")
    print("3.성적수정")
    print("9.성적파일저장")
    print("0.프로그램종료")
    print("-"*60)
    choice = int(input("원하는 번호 입력:"))
    return choice


#학생입력받기/add(클래스와 함수 연결)
def stu_input():
    global stuNum
    while True:
        print()
        print("[학생성적입력]")
        no=stuNum
        name = input(f"{stuNum}번째 학생이름(0.이전페이지 이동)")
        if name=="0":break
        kor = int(input("국어"))
        eng = int(input("영어"))
        math = int(input("수학"))
        total=kor+eng+math
        avg=total/3
        stus.add(Student(no,name,kor,eng,math))  #(리스트에넣기(객체 만들기))
        print(f"{stuNum}{name}학생 성적이 저장되었습니다.")
        print()
        stuNum+=1


#학생성적출력,Students객체
def stu_output():
    stus.print()



#학생성적 검색해서 점수를 수정하는 함수
def stu_update():
    print()
    print("[학생성적수정]")
    name=input("학생이름 검색:")
    temp =0
    for s in stus.slist:      #학생 리스트에서 학생을 한 명씩 꺼냄
        if s.name ==name:
            temp=1      #임시로 사용하는 변수--학생을 찾았는지 못찾았는지 확인하기 위해
            print(f"{name}의 학생이 검색되었습니다.")
            print("[수정과목]")
            print("1. 국어 2. 영어 3. 수학")
            print("-"*60)
            choice=input("과목을 선택하세요(0.취소)")
            if choice ==0: break
            elif choice ==1:
                print("[점수변경]")
                print("현재점수",s.kor)
                s.kor = int(input("변경 할 점수 입력:"))
            elif choice ==2:
                print("[점수변경]")
                print("현재점수",s.eng)
                s.eng = int(input("변경 할 점수 입력:"))
            elif choice ==3:
                print("[점수변경]")
                print("현재점수",s.math)
                s.math = int(input("변경 할 점수 입력:"))

                s.s_total()                           #호출로 총점과 평균을 다시 계산
                s.s_avg()
                print("수정이 완료되었습니다.")
                print()

    if temp==0:
        print(f"{name}학생이 없습니다. 다시 검색하세요.")
