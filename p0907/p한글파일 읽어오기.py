#abc출력하시오.
with open("c:/aaa/abc.txt","r",encoding="utf-8")as f:
    while True:
        str = f.readline()
        if str =="":break
        print(str,end="")





#----------------------------------------------------------------------------------#
#aaa.txt 출력
# sum=0
# with open("c://aaa/aaa.txt","r",encoding="utf-8") as f:
#     while True:
#         str= f.readline()
#         if str == "":break
#         str=str.strip()     #공백제거
#         if str.isdigit():
#             str = int(str)
#             sum += str

#     print("합계",sum)


#-------------------------------------------------------------------------------------#

#stu.txt 출력하시오
# f=open("c:/aaa/stu.txt","r",encoding="utf-8")
# while True:
#     str = f.readline()
#     if str =="":break
#     print(str,end="")
#f.close()

# stulist=[]
# with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
#     while True:
#         str=f.readline()
#         if str == "": break
#         stu=str.split(",")  # ,(쉼표)를 기준으로 리스트 생성
#         for i,s in enumerate(stu):
#             if i ==0 or i==1: continue
#             elif 2<=i<=5:
#                 stu[i]= int(s.strip())
#             elif i==6:
#                 stu[i] = float(s.strip())  #/n
            
#         stulist.append(stu)

#     print("파일읽어오기 완료!!")
#     print(stulist)

#--------------------------------------------------------------------------------------------#

#한글은 꼭, encoding="utf-8"
#with 파일읽어오기 - close 생략가능
# with open("c:/aaa/abc.txt","r",encoding="utf-8") as f:
#     while True:
#         str=f.readline()
#         if str=="":break
#         print(str,end="")

#open() 파일읽어오기
# readfile = open("c:/aaa/abc.txt","r")

# while True:
#     str = readfile.readline()                #readline- 한줄씩 가져오는형태
#     if str == "": break
#     print(str,end="")
# readfile.close()
#print("프로그램종료")

