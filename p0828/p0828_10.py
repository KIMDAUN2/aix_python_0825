# #반복문을 사용해서 1-100 까지 합을 출력하시오.
# sum=(0)

# for i in range(1,101):
#     sum= i + 1
#     print(sum)

# #200을 넘는 시점의 i의 값과 i번째 합계를 출력하시오.
# sum=0
# for i in range(1,200):
#     print(i)
#     sum=sum+i
#     if sum>=200:
#         print("200을 넘는 시점 :",i)
#         print("200을 넘는 i값의 합계:",sum)
#         break



# #200을 넘는 이전 시점의 i, 합계를 출력하시오.
# sum=0
# for i in range(1,200):

#     print(i)
#     sum=sum+i
#     if sum>=200:
#         print("200을 넘는 이전 시점 :",i-1)
#         print("200을 넘는 이전 i값의 합계:",sum-i)
#         break

# #구구단을 출력하시오
# for i in range(1,10):
#     for k in range(1,10):
#         print("{}X{}={}".format(i,k,i*k))



#여러명의 이름과 점수를 받을 때
#반복문은 리스트로 받아야 사용할 수 있다

#첫번째 방법
# name=[]
# kor=[]
# for i in range(2):
#     name.append(input("이름:"))
#     kor.append(int(input("국어점수:")))

# for i in range(2):
#     print("{}\t{}\t".format(name[i],kor[i]))
#두번째 방법
# stu=[]
# for i in range(2):
#     no=i+1
#     name=(input("이름:"))
#     kor=int(input("국어점수:"))
#     stu.append([no,name,kor])

# for i in range(2):
#     print("{}\t{}\t{}\t".format(*stu[i]))                                      #59,60번 둘중 아무거나 사용 가능
#     print("{}\t{}\t{}\t".format(stu[i][0],stu[i][1],stu[i][2]))
    