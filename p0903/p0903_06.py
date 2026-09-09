my_info={"id":"aaa","pw":"1111","name":"홍길동","money":10000000}

s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2


def p_cal(choice):
    if my_info['money']<s_arr[choice-1]['price']:
        print("보유금액이 부족합니다.")
        return
    print(f"구매상품: {s_arr[choice-1]["prd_name"]}")
    print(f"가격: {s_arr[choice-1]['price']}")
    my_info['money']-=s_arr[choice-1]['price']
    print(f"상품 구매 후 보유잔액:{my_info['money']}")

while True:
    print("[쇼핑몰에 오신걸 환영합니다.]")
    id=input("아이디:")
    pw=input("패스워드:")

    if my_info['id']==id and my_info['pw']==pw:
        print("로그인되었습니다.")
        break
    else:
        print("아이디 또는 비밀번호가 일치하지 않습니다.")

while True:
    for i,v in enumerate(s_arr):
        print(f"{i+1}.{v['prd_name']}:{v['price']:,}원")
    choice = int(input("원하는 번호입력 : "))
    if choice == 1:
        p_cal(choice)
    elif choice == 2:
        p_cal(choice)
    elif choice == 3:
        p_cal(choice)
    elif choice == 4:
        p_cal(choice)