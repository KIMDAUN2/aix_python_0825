#변수,함수 모두 포함해서 구현
#클래스 클래스변수:(클래스변수는 앞글자 대문자)
#장점- 데이터보호
class Car:
    color =""
    speed = 0
    tire = 0
    door = 0

    #생성자-생성함수 : Car() 선언될 때 실행되는 함수
    def __init__(self,color,speed,tire,door):
        self.color = color
        self.speed = speed
        self.tire = tire
        self.door = door


    def upspeed(self):      #self는 변수가 들어가있는 곳
        self.speed += 10

    def downspeed(self):
        self.speed -= 10


#-------------------------------------------
#클래스 1개 생성  /설계도(변수,함수)1번 작성 후 클래스 선언
c = Car("white",100,5,3)                   #객체(인스턴스) 생성 / 4개변수,2개함수 만들어짐
c.color ="white"         
c.speed =100
c.tire =5
c.door =3
c.upspeed()

#클래스 객채선언
c2 = Car("skyblue",200,4,5)
c2.upspeed()

c3 = Car("gray",50,5,5)
c3.upspeed()