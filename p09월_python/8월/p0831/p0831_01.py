#반복문
# #for i in range(1,10) / range(10)  /range(1,11,2)  / [1,2,3]   / "안녕하세요"
#구구단 출력
# for i in range(2,10):
#     print(i,"x",1,"=",i*1)
#     print("{}x{}={}".format(i,1,i*1))
#     print(f"{i}x{1}={i*1}")

#중첩for문
# for i in range(2,10):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="  ")
#     print()
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="\t")
#     print()



# 옆칸으로 출력
# print(1,end="\t")
# print(2,end="\t")
# print(3)





# nums = [3,9,10,105,220,2,1]
# for n in nums:
#     print(n)
#     if n%2==0:
#         print(n,":짝수입니다.")
#     else:pass
        # print(n,":홀수입니다.")
#짝수만 나오게 하고싶다면 pass



#입력한 숫자가 홀수인지, 짝수인지 출력하시오.
# a=int(input("숫자입력:"))
# if a%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")







# for i in "안녕하세요":
#     print(i)




# for i in range(1,11):
#     print(i*10)


# arrs=[1,3,5,7]
# for arr in arrs:
#     print(arr)

# fruits = ["사과","배","바나나"]
# for f in fruits:
#     print(f)





#이름입력을 3번 반복하시오.
# name=[]
# for i in range(3):
#     a= input("이름입력:")
#     name.append(a)  #리스트: append,insert,extend  -> 추가하기

# print("[ 학생명단 ]")
# print(name)
# for n in name:
#     print(n)
    


# for i  in range(3):  #기본 for문
#     print(i)


# for i in range range(1,5+1):  #1부터 5까지
#     print(i)
# print("-"*10)
# for i in range(1,11,2):
#     print(i)