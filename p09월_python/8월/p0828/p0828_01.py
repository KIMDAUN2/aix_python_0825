#번호 이름 국어 영어 수학을 입력받아,
#합계와 평균을 구한다음에
#성적을 출력하도록 구성하시오.

#입력-변수저장-DB저장
s=[] #리스트타입 - append,insert(추가) / pop,del,remove (제거)

no=input("번호입력:")
name=(input("이름입력:"))  #str
kor=int(input("국어점수 입력:"))
eng=int(input("영어점수 입력:"))   
math=int(input("수학점수 입력:"))
total=kor+eng+math
avg=total/3 #나눗셈 ->float형태로 나타남

print("[학생성적프로그램]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)  #문자*반복
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}")
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no,name,kor,eng,math,total,avg))


