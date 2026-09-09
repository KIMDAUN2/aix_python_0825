# no1=int(input("번호>>"))
# name1=input("이름>>")
# kor=int(input("국어점수>>"))
# eng=int(input("영어점수>>"))
# math=int(input("수학점수>>"))
# total=kor+eng+math
# avg=total/3

# no2=int(input("번호>>"))
# name2=input("이름>>")
# kor2=int(input("국어점수>>"))
# eng2=int(input("영어점수>>"))
# math2=int(input("수학점수>>"))
# total2=kor2+eng2+math2
# avg2=total/3

# no3=int(input("번호>>"))
# name3=input("이름>>")
# kor3=int(input("국어점수>>"))
# eng3=int(input("영어점수>>"))
# math3=int(input("수학점수>>"))
# total3=kor3+eng3+math3
# avg3=total/3


# print ("*"*80)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2d}".format(no1,name1,kor,eng,math,total,avg))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2d}".format(no2,name2,kor2,eng2,math2,total2,avg2))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2d}".format(no3,name3,kor3,eng3,math3,total3,avg3))







# a=int(input("점수"))
# if a >=60 :
#     print("합격")
# elif 50<=a<=59:
#     print("재시험")
# else:
#     print("불합격")








# import random
# a=random.randint(1,100)
# print("점수: ",a)
# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("F")



# import random
# a=random.randint(1,100)
# if a>=90:
#     if a >=98:
#         print("A+")
#     elif a>=93:
#         print("A")
#     else:
#         print("A-")
# elif a >=80:
#     if a >=88:
#         print("B+")
#     elif a >=83:
#         print("B")
#     else:
#         print("B-")
# else:
#     print("F")
# print("랜덤번호:",a)




import random
a=random.randint(1,10)
num=[]
nu=int(input("1번째 랜덤:"))
num.append(nu)
nu2=int(input("2번째 랜덤:"))
num.append(nu2)
nu3=int(input("3번째 랜덤:"))
num.append(nu3)

print()
print("랜덤숫자:",a)
print("선택숫자:",num)

if a in num:
    print("당첨")
else:
    print("꽝")

    