#반복문
# print("1",end=""\t)
# print("2",end="")
# print("3",end="")
# print("번호:",i+1,end="\t")   #옆으로출력

#구구단
# for i in range(1,10):             
#     print(f"2 X {i}={2*i}")
#

# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             print("{}X{}X{}={}".format(i,j,k,i*j*k))

#앞에 번호를 적으세요.
# for i in range(1,10):
#     for j in range(1,10):
#         print((i*10)+j+1,":",i,j)


#번호표001
# for i in range(1,10):
#      for j in range(1,10):
#          for k in range(1,10):
#              print("번호표")
#              print("{}{}{}".format(i,j,k))









# 합계가 100넘어가는 시점은 i가 얼마일때?
# sum=0
# for i in range(1,11):
#     print(i)
#     sum = sum+i
#     if sum>=11:
#         print("10보다 클 때: ",i)
#         print("10초과될때 시점 :" ,sum)   #1-10 =55/ 1-100=5050 / 1-1000=500500 / 1-10000=50005000
#         break

# 합계가 100초과되기 전 시점
# sum=0
# for i in range(1,11):
#     print(i)
#     sum = sum+i
#     if sum>=11:
#         print("10보다 크기 바로 앞일때: ",i-1)
#         print("10초과 전 시점 :" ,sum-i)  
#         break


#3명의 번호,이름,국어점수
# for i in range(3):
#     print(i+1,"번째")
#     no = i+1
#     name= input("이름입력 :")
#     kor=int(input("국어점수 입력:"))
#     print("{}\t{}\t{}".format(no,name,kor))




# for i in range(10):
#     print("안녕")

# for _ in range(10):
#     print("안녕")




# for 변수 in 범위 :
# for i in range(5):        #0,1,2,3,4
#     print(i)

# for i in range(0,5):      #0,10,20,30,40
#     print(i*10)

# for i in range(7,12):     #7,8,9,10,11
#     print(i)

# for i in range(0,10,2):    #0,2,4,6,8
#     print(i)

# for i in [1,5,3,2]:        #1,5,3,2
#     print(i)

# for i in "안녕하세요":       #안녕하세요
#     print(i)

# arr= list(range(1,11))     #[1,2,3,4,5,6,7,8,9,10]
# print(arr)

