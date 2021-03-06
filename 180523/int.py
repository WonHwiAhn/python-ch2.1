# 2진, 10진, 8진, 16진 상수(literal)

a = 23
print(type(a))
print(isinstance(a, int))

b = 0b1101
c = 0o23
d = 0x23

print(a, b, c, d)

# 3.x에서는 int와 long이 합쳐졌다. 따라서 표현범위는 무한대
e = 2**1024
print(type(e))
print(e.bit_length())

# 변환 함수
print(oct(38))
print(hex(38))
print(bin(38))