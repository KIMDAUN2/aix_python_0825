# 파일복사하기     rb((파일)바이너리 읽기)  r(문서로읽겠다)   wb(바이너리 쓰기)
import os

#---------------------리센느사진---------#
# rf = open("c:/aaa/1.jpg","rb")
# wf = open("c:/aaa2/2.jpg","wb")

# while True:
#     fdata = rf.read(1)
#     if not fdata:break
#     wf.write(fdata)

# rf.close()
# wf.close()

#-------------------스위스사진-----------#
print("이미지파일이 복사되었습니다.")

rf = open("c:/aaa/3.jpg","rb")
wf = open("c:/aaa2/4.jpg","wb")

while True:
    fdata = rf.read(1)
    if not fdata:break
    wf.write(fdata)

rf.close()
wf.close()