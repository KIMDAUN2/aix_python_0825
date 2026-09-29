#변수,리스트,딕셔너리 선언부분
#개인정보
my_info = {"id":"aaa","pw":"1111","money":10_000_000,"bonusPoint":0}
# 구매리스트
cart = []
# 상품
product = [
    {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
    {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
]


def cal(choice):
    no=int(input(("컴퓨터를 구매하시겠습니까?(구매:1,취소:0)")))
    if no== 1:
        print(f"{product[choice-1]['p_name'] }컴퓨터 구매완료")
        #계산후 결과
        my_info['money'] -= product[0]['price']
        # my_info['money'] = my_info['money'] - product[0]['price']
    
        my_info['bonusPoint'] += product[0]['bonusPoint']
        print(f"m머니 : {my_info['money']:,}원")
        print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
    else:
        print("이전화면으로 이동합니다.")




# 아이디,패스워드 확인
while True:
    print("[ 쇼핑몰에 오신것을 환영합니다. ]")
    id = input("아이디 : ")
    pw = input("패스워드 : ")

    if my_info["id"] == id and my_info["pw"]==pw:
        print("로그인이 되었습니다.")
        break
    else:
        print("아이디 또는 패스워드가 일치하지 않습니다.")

#현재 나의 정보-금액,보너스포인트
print(f"현재 보유금액 : {my_info['money']:,}원")
print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
print("-"*40)

#구매정보
while True:
    print()
    #상품출력부분
    print("[쇼핑몰 구매사이트]")
    for i,p in enumerate(product):
        print(f"{i+1}.{p['p_name']} :{p['price']:,}원")
    print("9.구매상품리스트")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>>"))
    print()
    #1.컴퓨터 구매부분
    if choice==1:
        cal(choice)
    elif choice == 2:
        cal(choice)
    elif choice ==3:
        cal(choice)
    else:
        print("이전화면으로 이동합니다.")






















#일반 매개변수, 초기화 매개변수, 가변매개변수, 키워드 매개변수

# def cal(s1=1,e1=50,s2=10): #초기화매개변수
#     print(s1,e1,s2)

# cal(0)             #0 50 10
# cal(100,1,2)       #100 1 2
# cal(1,2,s2=100)    #키워드매개변수 -> 1 2 100








#가변매개변수-일반변수 뒤에 배치
#키워드매개변수- 맨뒤쪽에 배치,앞에배치하면 에러
#리턴- 함수를 실행했던 위치로 돌아가게 함,값이 있으면 같이 넘어감

# def str_print(*v,n):  #가변매개변수
#     print(n)
# str_print(1,2,3,4,5,n="안녕")  



# print(1,2,3,4,5, sep="/")  #1/2/3/4/5
# arr = ["번호","이름","국어","영어"]
# print(*arr,sep="\t")  #번호    이름    국어    영어   (전개연산자,키워드매개변수)


# def str_print(n,*v): # 매개변수 2개, 가변매개변수(개수 맞추지 않아도 된다.)
#     for i in range(n):
#         for j in v:
#             print(j,end="")
#         print()

# str_print(3,"안녕","반가워","잘있어")