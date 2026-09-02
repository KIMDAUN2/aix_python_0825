#빙고게임 형식
alist = list(range(1,26))
# print(alist)
for i in range(len(alist)):      #25번 반복
    if (i+1)%5 != 0 :
        print(alist[i],end="\t")
    else:
        print(alist[i])



#1-25까지 리스트를 생성하고
#랜덤으로 리스트를 섞은 다음, 5개씩 2차원리스트를 만드시오.
# import random
# alist = list(range(1,26))
# random.shuffle(alist)
# alist2 = []
# for i in range(0,len(alist),5):
#     alist2.append(alist[i:i+5])
# print(alist2)



# aa="abcdefabcdefabcdefabcdefabcdef" #30
# aa2 =[] #3개씩 나눠서 저장하시오.
# for i in range(0,len(aa),3):
#     aa2.append(aa[i:i+3])
# print(aa2)




#1차원리스트를 2차원리스트 형태로 구성
# arr = [1,2,3,4,5,6,7,8,9]  #len(arr)=9
# arr2 = []
# for i in range(0,len(arr),3):
#     arr2.append(arr[i:i+3])    #0,1,2
# print(arr2)
#위 정답.
# arr2 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]