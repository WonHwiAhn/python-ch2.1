# 사칙연산
print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3) # 정수 나누기 정수도 실수 값이 나옴.
print(2 / 3.0)

# // <= 몫 연산자, ++ <= 지수승, % <= 나머지 연산
print("----몫 연산자----")
print(2//3)
print(2 ** 3)
print(2 % 3)

# divmode() 함수
print("----divmode----")
print(divmod(2, 3))

# 연산자 우선순위
print("----연산자 우선순위----")
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

print(4 / 2 * 2)

# 결합순서
print("----결합순서----")
print( 2 ** 3 ** 4)
print((2 ** 3) ** 4)
print(2 ** (3 ** 4))