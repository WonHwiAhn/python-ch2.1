a = 1.2
print(type(a))
print(isinstance(a, float))

# 객체함수 is_integer()는 값으로 정수인지 실수인지 확인한다.
# 타입을 확인하는 함수가 아니다.
b = 2.0
print(b.is_integer())

b = 3e3
c = -0.2e-4

# 다른 언어처럼 소수점이나 e, E로 지수 표현이 가능하다.
print(a, b, c)