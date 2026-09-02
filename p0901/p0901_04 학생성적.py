# # 로또맞추기

# import random
# lotto = random.sample(range(1,46),6)
# print("확인:",lotto)
# in_arr=[]
# no=0
# for i in range(6)
#     no = int(input"숫자입력:)




# # [1,2,3,4,5,6,7,8,9]   1차원리스트
# # 리스트- 직접입력,[0]*10, list(range(1,10))
# num_arr = list(range(1,10))
# print(num_arr) 
# all_arr=[]
# for i in range(0,9,3):   #0,3,6
#     print(i,end=" ")    #0,3,6
#     all_arr.append(num_arr[i:i+3])
# #     # all_arr.append(num_arr[0:0+3])    #0-3 :0,1,2
# #     # all_arr.append(num_arr[3:3+3])    #3-6:3,4,5
# #     # all_arr.append(num_arr[6:6+3])    #6-9:6,7,8
#     print(all_arr)




#####################################
#학생성적프로그램
#학생성적입력- 변수,리스트-리스트,리스트-딕셔너리
#stu_list=[
    # ([1,"홍길동",100,100,100,300,100.0]
    # [2,"유관순",100,100,100,300,100.0]
    # [3,"이순신",100,100,100,300,100.0])
#]
#---------------------->>
# stu_list =[]
# stu_list.append([1,"홍길동",100,100,100,300,100.0])
# # for문
# for i in range(3):
#     no=input("번호입력")
#     name=input("이름입력")
#     kor = int(input("국어입력"))
#     eng = int(input("영어입력"))
#     math = int(input("수학입력"))
#     total = kor+eng+math
#     avg=total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print(stu_list)

#while문 
# while True:
#     no= len(stu_list)+1      #자동 숫자입력, 앞번호 지우면 번호 중복되는 단점이 있음.
#     print("자동번호:",no)
#     name=input("이름입력(종료하려면 0)")
#     if name == "0":break
#     kor = int(input("국어입력"))
#     eng = int(input("영어입력"))
#     math = int(input("수학입력"))
#     total = kor+eng+math
#     avg=total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print("입력된 학생성적 :",len(stu_list))
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)
# for s in stu_list:
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))