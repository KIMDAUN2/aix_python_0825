#파일 읽어오기
f=open("C:\\aaa\\test1.txt","r",encoding="utf-8")   #\\=/     #r=읽기모드 encoding-깨지지 않도록 utf-8방식으로 읽겠다 라는 뜻
while True:
    line = f.readline()
    if not line: break
    print(line,end="")
f.close()

