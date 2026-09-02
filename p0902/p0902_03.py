#isdigit() : 숫자인지 확인/isalpha(),isalnum()
while True:
    a=input("숫자를 입력하세요.")
    if a.isdigit():
        a =int(a)
        break
    else:
        print("숫자가 아닙니다.다시 입력하세요")
print(a)


#split 분리, *전개연산자
# str =(input("날짜를 입력하세요.(2026/09/02)"))
# str_arr= str.split("/")
# print("{}년 {}월 {}일". format(*str_arr))
#2026년9월2일



##---------------------------------------------------------------##
# #map,join  -> 문자열
# stu = [1,"홍길동",100,100,100]
# stu = list(map(str,stu))   #map 특정한 함수로 반복해줌.
# #, 구분해서 문자열로 저장하시오.
# stu = ",".join(stu)
# print(stu2)
##--------------------------------------------------------------##





# #map(함수,반복리스트)
# aa=['1','2','3']
# print(list(map(int,aa)))   #aa를뽑아서 인트로 변경해줌(맵->리스트)


# #3개의 합을 구해서 출력하시오.
# str = input("번호 3개를 입력하세요,(123/5/23)>>")
# strlist=str.split("/")         #문자열타입
# strlist(list(map(int,strlist)))   #문자열 ->정수타입으로 변환
# sum=0
# for s in strlist:
#     sum+= s
# print(sum)