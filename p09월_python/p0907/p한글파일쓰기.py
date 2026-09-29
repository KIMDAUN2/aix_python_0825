# r-읽기, w- 덮어쓰기, a-이어쓰기
#파일쓰기(w) - 수정을 하면 기존 내용 사라짐
#input은 엔터키를 따로 쓰지 않으면 옆으로 넣어줌
#없는폴더에 추가하려고 하면 에러
import os

fname = input("저장할 파일이름을 입력하세요(폴더/파일명)>>>")


if not os.path.exists("common"):   #존재하지 않으면
    os.makedirs("common")          #폴더생성

with open("common/"+fname,"a",encoding="utf-8")as f:
    while True:
        ourstr = input("내용입력 : ")
        if ourstr == "": break
        f.write(ourstr+"\n")

print("파일내용이 저장되었습니다.")