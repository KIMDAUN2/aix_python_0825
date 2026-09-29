#common폴더 안에 stu.txt로 파일을 저장하시오
#1,홍길동,100,100,100,300,100.0 으로 나오게 만드시오

with open("common/stu.txt","a",encoding="utf-8") as f:
    allstr = ""
    no=0
    while True:    #,1,홍길동,100/  1,홍길동,100,
        ourstr=input("내용입력:")
        if no ==0:
            allstr += ourstr
            no+=1
            continue

        if ourstr =="":
            f.write(allstr+"\n")
            break
        allstr += (","+ourstr)
        no+=1
    print(allstr)
print("파일내용이 저장되었습니다.")