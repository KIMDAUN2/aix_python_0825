#예외처리
#1.조건문을 사용하는 방법
#2.try구문을 사용하는 방법 


#구문오류 - 실행전 발생하는 오류
#pront(1) 

#런타임에러-실행중 발생하는 오류(없는 번호를 입력할때) 
#try-except 방법(try:예외가 발생할 가능성이 있는 코드,except: 예외가 발생했을 때 실행할 코드)
#1.
# arr=[1,2,3,4,5]
# while True:
#     try:
#         choice = int(input("0-4까지 숫자입력:"))
#         print("선택값:",arr[choice])
#     except:
#         print("에러가 났습니다")


#2. 에러가 나지않으면 except의 결과는 나오지 않는다.
# print(1)
# try:
#     print(2)
#     print(3)
#     print(10/0)  #에러남
#     print(4)
# except:
#     print(5)
#     print(6)
# print(7)



#Exception -어느부분이 에러가 났는지 알려줌
#except Exception as e :
#        print(e)
#        print(type(e))


#조건문으로 예외 처리하기 
# arr=[1,2,3,4,5]
# while True:
#     choice = int(input("0-4까지 숫자입력:"))
#     if choice.isdigit():  #숫자로만 구성된 글자인지 확인
#         choice= int(choice)
#     else:
#         print("숫자만 입력가능합니다.")
#         continue
#     print(arr(choice))



#as=별칭


# choice = int(input("원하는 번호입력:"))
# if choice ==1:
#     print("학생성적입력부분")
# elif choice ==2:
#     print("출력")
# elif choice ==3:
#     print("수정")
# raise NotImplementedError



# print(1)
# print(2)
# print(3)
# raise NotImplementedError
# print(4)
# print(5)
# print(6)
# print(7)




