# name = []
# kor = []
# eng = []
# math= []
# total=[]
# avg=[]
# for i in range(3):
#     name.append(input("이름:"))
#     kor1=(int(input("국어점수:")))
#     kor.append(kor1)
#     eng1=(int(input("영어점수:")))
#     eng.append(eng1)
#     math1=(int(input("수학점수:")))
#     math.append(math1)
#     total.append(kor1+eng1+math1)
#     avg.append((kor1+eng1+math1)/3)

# print("[학생성적]")
# print("번호\t이름\t국어\t영어\t수학\t힙계\t평균\t")
# for i in range(len(name)):
#     print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{total[i]}\t{avg[i]:.2f}")













# list_a=["바나나","사과","딸기"]
# # j=1
# # for i in list_a:
# #     print(j,":",i)      #바나나,사과,딸기
# #     j=j+1


# # enumerate: index번호,리스트값 2개 전달,0번부터 시작
# for i,value in enumerate(list_a):   
#     print(i+1,":",value)

# for i in range(3):                    #괄호 안에 len(list_a) 라고 하면 안에 들어간 개수만큼 출력된다
#     print(i+1,":",list_a[i])



# for i in range(1,4):
#     print(i)      #1,2,3


#리스트 추가
# list_a=["바나나","사과","딸기"]
# for i in range(3):
#     list_a.append(input("과일입력:"))

# for i in list_a:
#     print(i)








#구구단을 출력하시오
# 숫자입력을 받아 입력받은 단부터 출력하시오.

# a=int(input("시작 단 입력:"))
# b=int(input("끝단 입력:"))
# for i in range(a,a+1):
#     for k in range(1,b+1):
#         print("{}X{}={}".format(i,k,i*k))






#입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합을 구하시오.
#2,5

# a=int(input("1. 숫자입력:"))
# b=int(input("2. 숫자입력:"))
# c=0
# if a>b:   #a가 클때만 값을 서로 변경
#     a,b=b,a
#     # c = a          #값변환
#     # a = b
#     # b = c
# for i in range(a,b+1):
#     sum = a+b
# print("합:",sum)




#3개의 입력한 숫자의 합을 구하시오
# sum=0
# ali=[]
# for i in range(3):
#     a=int(input("숫자 입력:"))
#     ali.append(a)
#     sum= sum+ a

# print("합계:",sum)
# print("입력값:",ali)





#1에서100까지의 합을 구하시오
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print("합: ",sum)




#홀수 합을 구하시오
# sum=0
# for i in range(1,101,2):
#     sum=sum+i
# print("합: ",sum)




#7의 배수만 합을 구하시오
# sum=0
# for i in range(1,101):
#     if i%7==0:
#         print(i)
#         sum=sum+i
# print("합: ",sum)


# sum=0
# result =1
# for i in range(1,11):
#     sum=sum+i
#     result=result*i

# print("합계:",sum)
# print("곱:{:,}".format(result))



#sum 이 100 넘을때 i값 출력하시오
# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#     sum=sum+i
#     if sum >= 100:
#         no=i
#         sum2= sum
#         break



#sum 이 100 넘기 전 i의 값 출력하시오
# print("합계가 100을 넘을 때 i의 값:",no)
# print("그 때의 합계 :",sum2)

# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#     sum=sum+i
#     if sum >= 100:
#         no=i
#         sum2= sum
#         break

# print("합계가 100을 넘기 전 i의 값:",no-1)
# print("이전단계 합계 :",sum2-no)

#구구단을 아래로 출력하시오.
# for i in range(2,10):
#     print(f"[{i}]",end="\t")
# print()
# for i in range(1,10):
#     for j in range(2,10):
#         print("{}x{}={}".format(j,i,i*j),end="\t")
#     print()    #공백처리