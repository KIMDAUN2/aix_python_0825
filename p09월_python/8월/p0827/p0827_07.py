# 원하는값 in 리스트, 원하는값 not in 리스트
arr = [1,3,5,7,9]
if 7 in arr:
    print("원하는 수가 있습니다.")
else:
    print("원하는 수가 없습니다.")

if 6 not in arr:
    print("원하는 수가 있습니다.")
else:
    print("원하는 수가 없습니다.")


# 정렬 순차정렬(sort), 역순정렬 sort(reverse=True)
# arr =[1,15,8,23,2]
# arr.sort()
# print(arr)          #[1,2,8,15,23]
# arr.sort(reverse=True)
# print(arr)          #[23,15,8,2,1]

#리스트삭제-del,pop,remove,clear(모두삭제)
# arr = [1,2,3,4,5,True,"안녕"]
#pop
# print(arr)    #[1,2,3,4,5]
# arr.pop(2)    #2번주소삭제
# print(arr)    #[1,2,4,5]
#del
# del arr[0]      #0번주소삭제
# print(arr)      #[2,3,4,5]
#remove
# arr.remove("안녕")


#리스트 추가
# a=[1,2,3]
# b=[4,5,6]
#원본에 영향이 없음
# print(a+b)     #[1,2,3,4,5,6]
# print(a)       #[1,2,3]
#원본의 값을 직접 변경해서 추가해줌 
# a.extend(b)
# print(a)       #[1,2,3,4,5,6]


# 리스트추가 :append,insert
#append: 제일 뒤에 추가
# arr =[1,2]
# arr.append(3)
# arr.append(9)
# arr.append(5)
# print(arr)            #[1,2,3,9,5]
#arr = [1,2,3,9,5]
#insert : 원하는 위치에 추가
# arr.insert(1,20)      
# print(arr)            #[1,20,2,3,9,5]


# arr1 = [1,2,3]
# arr2 = [4,5]
# arr3 = arr1+arr2     
# print(arr1+arr2)      #[1,2,3,4,5]
# print(arr3)           #[1,2,3,4,5]

#반복
# arr4= arr1*3
# print(arr4)            #[1,2,3,1,2,3,1,2,3]

# aaa = [0,0,0,0,0,0,0,0,0,0]
# aaa2 = [0]*10





#2차원배열
# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(arr[1])     #[4,5,6]
# print(arr[1][1])  #[5]


#문자열-리스트형태로 저장
# name = "안녕하세요반갑습니다."
# print(name)        #안녕하세요반갑습니다.
# print(name[1])     #녕
# print(name[6])     #갑
# print(name[5:7])   #반갑습
# print(name[::-1])  #.다니습갑반요세하녕안
# print(name[::2])   #안하요갑니.
# if"하" in name:
#     print("있습니다.")
# else:
#     print("없습니다.")

# fruit = ["사과","딸기","수박","참외","복숭아"]
# print(fruit[2])   #2번
# print(fruit[1:4]) #1,2,3
# print(fruit[2:])  #2번부터끝까지 출력
# print(fruit[:3])  #0번부터2번까지 출력
# print(fruit[:])   #모두출력

# 슬라이싱 [시작:끝:간격]
# print(fruit[::2]) #간격 -> 사과,수박,복숭아
# arr=[1,2,3,4,5,6,7,8,9]
# print(arr[::2])  #홀수 ->1,3,5,7,9
# print(arr[1::2]) #짝수 ->2,4,6,8
# print(arr[:-1])    #마지막제외 나머지 출력
# print(arr[::-1])   #리스트 역순정렬



# import random
# r_num = random.randint(1,5)
#3개 숫자입력
# arr= []
#리스트에 값을 추가할 시 append 사용
# arr.append(int(input("1. 1-10 숫자입력: ")))
# arr.append(int(input("2. 1-10 숫자입력: ")))
# arr.append(int(input("3. 1-10 숫자입력: ")))
#1.
# if r_num in arr:
#     print("당첨")
# else:
#     print("꽝")
# print("랜덤숫자 : ",r_num)
# print("입력숫자 :",arr)

# #2.
# if r_num in arr: print("당첨")
# else:print("꽝")
# #3.
# print("당첨")if r_num in arr else print("꽝")




# 비교시 리스트는 ("검색내용" in 리스트) 하면 됨.
#a,b,c,d,e 중 참외가 있는지 확인하고, 있으면 참외가 있습니다.
#참외가 없으면 참외가 없습니다.
# a="사괴"
# b="딸기"
# c="수박"
# d="참외"
# e="복숭아"

# if a=="참외" or b=="참외" or c=="참외" or d=="참외" or e=="참외":
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")

# 리스트
# fruit = ["사과","딸기","수박","참외","복숭아"]
# if "참외" in fruit:                  #과일안에 참외가 있는지 확인
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")


# 1-10사이의 숫자 3개를 입력받아
#랜덤숫자를 맞추면 당첨,그렇지 않으면 꽝

#반복문을 사용할 수 없음.
#일반변수는 반복문을 사용하기 힘듬
# no1=int(input("1.숫자입력:"))
# no2=int(input("2.숫자입력:"))
# no3=int(input("3.숫자입력:"))
# print("입력숫자 :",no1,no2,no3)

# num=[0,0,0]   #리스트 숫자 3개입력할때
# num[0]=int(input("1.숫자입력:"))
# num[1]=int(input("2.숫자입력:"))
# num[2]=int(input("3.숫자입력:"))
# print("입력숫자 :",num)




# 리스트 추가가능 타입 : 모든타입가능
# arr=[1,"안녕",1.2,True,[1,2,3]]
# print(arr[1])     #안녕
# print(arr[3])     #True
# print(arr[4])     #[123]
# print(arr[4][1])  #2
# a= arr[4]
# print(a[1])       #2








#리스트=배열
# a=1
# arr=[1,2,3,4,5]
# print(type(a))    #int
# print(a)          #1
# print(a+1)        #2
# print(type(arr))  #list
# print(arr)        #[1,2,3,4,5]
# print(arr[1]+1)   #3
# print(arr[2])     #3
# print(len(arr))   #리스트 개수 length 줄임.
#리스트는 [] 로 시작
#리스트는 여러개를 저장할 때 사용
#리스트는 0번부터 주소가 시작
#리스트를 print하면 모두 출력가능
#리스트의 특정주소로 그 값을 출력할 수 있음
#리스트 개수 : len()
#리스트 안에는 모든 타입을 넣을 수 있음 - 정수,실수,문자열,불,리스트,튜플,딕셔너리
