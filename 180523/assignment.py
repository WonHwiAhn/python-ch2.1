# 치환문 예

a = 1
b = a + 1
print(a, b)

# 변수값 할당 오류
# 1 + a = c

# 세미콜론을 이용해 한 줄로 적을 수 있으나 파이썬 규칙에 위배
a = 3.5; f = 5.3
print(a, f)

# 여러개를 한 번에 치환
a, f = 3.7, 4.1
print(a,f)

# 같은 값을 여러 변수에 할당할 때
x = y = z = 10
print(x, y, z)

# C 스타일
# x = (y = 10)

# 값 교환
f, a = a, f
print(f, a)

# 동적 타이핑: 변수에 새로운 값이 할당되면 기존의 값을 버리고
# 새로운 값으로 치환된다.
a = '1'
print(type(a))

# 확장 치환문
a = 10
a += 10
print(a)

a -= 3
print(a)

