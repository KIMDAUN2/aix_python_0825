# alist = []              #0
# print(len(alist))
# alist2 = [0,0,0]        #3개
# print(len(alist2))
# alist3 = [0]*10         #10
# print(len(alist3))
# alist4 = list(range(10))#[0,1,2,3,4,5,6,7,8,9]
# print(alist4)
alist5 =[i*i for i in range(10)]   #리스트 내포
print(alist5)




# for i in range(10): #range(1,11,2)/[리스트]/문자
#     print(i)


#enumerate 사용 리스트 출력
#번호,값 2개가 동시에 전달이 됨
# a_list=["딸기","바나나","사과"]
# for i,value in enumerate(a_list):
#     print("{}:{}".format(i+1,value))