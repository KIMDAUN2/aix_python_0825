# vscode에서 로컬디스크 폴더에 파일 저장하기(안에 글 넣어서)
# r : 파일 읽기 , w : 파일덮어쓰기 , a:이어쓰기
with open("c:/aaa/abc.text","a") as f:
    while True:
        line = input("글을 입력하세요.")
        if line != "":
            f.writelines(line+"\n")  #\r : 문장끝으로, \n: 줄바꿈
        else:
            break

print("파일이 저장되었습니다.")