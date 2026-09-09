stu=[]
f=open("C:\\aaa\\test2.txt","r",encoding="utf-8")   #\\=/
while True:
    line = f.readline()  #\n 줄바꿈떄문에 에러가 남.    #한줄 읽어오기
    if line=="": break
    line=line.strip()   #공백제거
    #"1,홍길동",100,100,100,300,100.0"
    #문자열을 각각의 문자열로 분리
    print(line,end="")
    arr = line.split(",")   #분리하기

    for i,a in enumerate(arr):
        if 5>= i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i]=float(a)
    #stu 리스트에 저장
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],"avg":arr[6]})
f.close()
print(stu)