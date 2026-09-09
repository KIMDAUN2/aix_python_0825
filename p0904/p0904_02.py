#기본함수사용
# def sum(n1,n2):
#     result = n1 + n2
#     return result
# print(sum(10,20))      #n1=10  n2=20


#람다식 - 함수요약
#람다식-1줄만 명령어가 있어야 함.                (매개변수:리턴값)
#def이가lambda라고 생각하고 넣고 변수: 수식
#매개변수는 여러개여도 되는데 수식은 하나만 가능
#1.
# sum = lambda n1,n2:n1+n2           
# print(sum(10,20))
2.
# sum = lambda n1:n1+10
# print(sum(10))




#기본구성
#1.
# mlist = [1,2,3,4,5]   #+10
# mlist2 = []
# for m in mlist:
#     mlist2.append(m+10)
2.
# def add(num):
#     return num+10

# mlist =[1,2,3,4,5]
# a_arr= []
# for m in mlist:
#     a_arr.append(add(m))


#리스트내포
# a_arr = [m+10 for m in mlist]
# print(a_arr)




#map -> ㅡmap은(함수,리스트)
# a_lam=lambda num:num+10   #람다식으로 map쓰기
# mlist =[1,2,3,4,5]
# mlist2=list(map(lambda num:num+10,[1,2,3,4,5]))      ##이것만 외우기
# print(mlist2)                      #[11, 12, 13, 14, 15]

# data = ["100","200","300"]
# result = map(int,data)
# print(list(result))               #[100, 200, 300]


# a = [1,2,3]
# b=[10,20,30]
# result = map(lambda x,y:x+y, a,b)
# print(list(result))                 #[11, 22, 33]






#팩토리얼-자기 자신을 다시 호출하는 함수,재귀함수
#1-4 곱을 구하시오
# result =1
# for i in range(1,5):
#     result *= i
#     print(result)                      #24,fro문

# def fac1(num):
#     if num <=1:
#         return num
#     else:
#         return num * fac1(num-1)
# print(fac1(4))                            #24,재귀함수(팩토리얼)


