import keyword

# 변수 이름은 문자, 숫자, _로 구성된다.

friend = 1
a = 10
my_name = '안원휘' #밑에 my_name1 변수랑 같음
my_name1 = "안원휘"

_yourName = "둘리"
member1  = "도우넛"

#에러: 다른 구성의 변수 이름은 사용할 수 없다.
# friend$ = 1
# a! = 10
# 1abc = 10

#에러: 예약어는 변수 이름으로 사용할 수 없다.
# def = 10
# print = 20 # print는 경고만 뜨지만 run하면 에러남.


print(print)
print(keyword.kwlist)
print(len(keyword.kwlist))

# 한글 이름의 변수도 사용 가능하다
가격1 = 2000
print(가격1 - 200)