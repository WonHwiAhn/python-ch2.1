# ~ 부정 연산자
print(~5)
# 0000  0101
# 1111 1010

print(~-1)
print(~0)


# << 연산자
a = 4
print(a >> 1)


a = -4
print(a >> 1)
print(a << 1)


# bit and, or exculusive

a = 3

print(a & 2)
print(a | 2)
print(0x0f ^ 0x06)
