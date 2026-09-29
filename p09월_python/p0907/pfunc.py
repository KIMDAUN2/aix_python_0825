stulist=[]
title=["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title=['no','name','kor','eng','math','total','avg','rank']
stunum= 1


#파일불러오기
def readstu():
    global stunum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:      #파일 덮어쓰기
        while True:
            str = f.readline()
            if str =="":break
            stu = str.split(",")
            for i,s in enumerate(stu):           #문서이름 stu
                if 0<=i<=1: continue
                elif 2<=i<=5: stu[i]=int(s.strip())
                elif i==6: stu[i]=float(s.strip())
                elif i==7: stu[i]=int(s.strip())

            stulist.append(dict(zip(s_title,stu)))
            stunum = len(stulist)+1



def writestu():
    with open("c:/aaa/stu.txt","w",encoding="utf-8")as f:
        for s in stulist:
            str = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
            f.write(str+"\n")
        print("성적파일이 저장되었습니다.")
        print()





#메인
def main_screen():
    print("[학생성적프로그램]")
    print("1.성적입력")
    print("2.성적출력")
    print("3.성적수정")
    print("9.성적저장")
    print("0.성적종료")
    print("-"*60)
    print()
    choice=int(input("원하는 번호 입력:"))
    return choice

#성적입력
def stu_input():
    global stunum
    while True:
        print()
        print("[학생성적입력]")
        no=stunum
        name=input(f"{stunum}번째 학생이름(0.이전페이지)")
        if name == "0": break
        kor=int(input("국어:"))
        eng=int(input("영어:"))
        math=int(input("수학:"))
        total=kor+eng+math
        avg=total/3
        rank=0
        stulist.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{stunum}.{name} 학생성적이 저장되었습니다.")
        print()
        stunum +=1


def stu_output():
    print()
    print(" "*25,end="")
    print("[학생성적출력]")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    for s in stulist:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
        print()