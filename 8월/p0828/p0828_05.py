a = "11"
print(type(int(a)))        #<class.int>

b=1.12
print(int(b))        #정수만가져옴  1
print(float(b))      #1.12

c = 10
d = 3
e = 10/3         #나누기는 타입이 실수로 변경, 정수만 나오게 하려면// 몫으로 기호 쓰기
print(type(e))

f = 5
if f%2==0:
    print("짝수")
else:
    print("홀수")

result = "짝수" if f%2==0 else "홀수"         #한줄로 표현
print(result)