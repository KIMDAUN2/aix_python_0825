#아이디,패스워드를 입력받아 출력하시오,
#아이디:aaa #패스워드:1111
# id= input("아이디입력")
# pw= input("패스워드입력")
# print("아이디확인:{}".format("aaa==id"))
# print("패스워드확인:{}".format("1111==pw"))
# print("아이디:{},비밀번호{}".format(id,pw))

#잔액 :1000  송금:100 총금액:1100 출력되도록하시오.
# total=1000
# send=int(input("송금금액입력>>"))
# total2=total+send
# print("잔액:{},송금:{},총금액:{}".format(total,send,total2))

#이름,국어,영어,수학점수를 입력받아 합계,평균 출력
#합계=300, 평균=100
# name=input("이름입력")
# kor=int(input("국어점수입력"))
# eng=int(input("영어점수입력"))
# math=int(input("수학점수입력"))
# total=kor+eng+math
# avg=total/3
# print("이름:{},국어점수:{},영어점수:{},수학점수:{},합계:{},평균:{}".format(name,kor,eng,math,total,avg))


#번호,이름,극어,영어,수학 입력받아 합계 평균을 구하시오
# no1=int(input("번호입력"))
# name=input("이름입력")
# kor=int(input("국어점수입력"))
# eng=int(input("영어점수입력"))
# math=int(input("수학점수입력"))
# total=kor+eng+math
# avg=total/3
# print("*"*60)
# print("번호\t이름\t국어점수\t영어점수\t수학점수\t 합계\t 평균")
# print("*"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(no1,name,kor,eng,math,total,avg))

# a=int(input("숫자입력"))
# print(a%2==0)

#프로그램 종료 대문자 X또는 X를 입력
# str=input("프로그램을 종료하려면 입력하시오.")
# if(str=="X")or(str=="x"):
#     print("종료합니다")
# else:
#     print("다시 눌러주세요.")

#12340원에서 500원짜리 몇개,100원짜리 몇개, 10원짜리 몇개가 필요할까?
# money=12340
# result=money//500
# num=money%100
# result2=num//100
# num2=num%10
# result3=num//10
# print(result,result2,result3)