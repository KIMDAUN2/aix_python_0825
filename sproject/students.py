from student import s1,s2  #student에서 s1,s2를 가져와

class Students:
    stuList = []            #여러명을 리스트로 관리

    def add(self,s):        #s는 변수, 리스트에 추가
        self.stuList.append(s)

    def print(self):
        for s in self.stuList:
            s.s_total()
            s.s_avg()
            print(s)


#객체만들고,함수기능 사용하게 만들기
stus = Students()

stus.add(s1)
stus.add(s2)
        