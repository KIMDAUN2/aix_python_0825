a,b,c,d,e = 0,0,0,0,0
print(a)
print(b)
print(c)
print(d)
print(e)
print(a+b+c+d+e)

a_arr=[10,20,30,40,50,60,70,80,90,100]
sum = 0
for a in a_arr:
    print(a)
    sum+= a
print(sum)


#슬라이싱 사용
# print(a_arr[2:5])    #[30,40,50]
# print(a_arr[::-1])   #역순정렬


#리스트 추가 : append:뒤에 ,insert:위치 ,extend:리스트+리스트
#리스트 수정: a_arr[위치] =1000
#리스트 삭제: pop(위치): 위치가 없으면 제일 뒤에 삭제, del(위치)

# a_list = [1,2,3]
# a_list.append(4)     #[1,2,3,4]
# print(a_list)
# a_list.pop(0)        #[2,3,4]
# print(a_list)



# # 퀴즈
# n_arr = [100,91,230,1,2,5,70,500]
# # 100이상의 숫자만 출력하시오.
# # 100:3자리숫자
# # 91:2자리숫자
# # 230:3자리숫자
# # 1:1자리숫자
# a_arr = []
# for n in n_arr:  # n타입:정수형타입 -> 문자타입     #문자타입으로 해야 자릿수를 셀 수 있음.
#     no = len(str(n))
#     a = "{}:{}자리숫자".format(n,no)
#     a_arr.append(a)
#     print(a)
# print(a_arr) 



# for n in n_arr:
#     if n>=100:
#         a_arr.append(n)
#         print(n)

# print(a_arr)

# a =100
# b ="100"
# print(len(b))
# #print(len(a))   -> 에러 