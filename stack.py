# 스택으로 활용하기

stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

# 큐로 사용하기
q = [1, 2]

q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))
print(q.pop(0))
print(q)

# sort(): 객체함수 : 내장된 소팅 알고리즘에 따라 정렬
print('# sort(): 객체함수 : 내장된 소팅 알고리즘에 따라 정렬')
l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key=str)
# l.sort(key=int)
print(l)

# 내장(전역) 함수 : sorted
print('# 내장(전역) 함수 : sorted')
l = [19, 46, 37, 28, 91, 55, 64]
l2 = sorted(l)
print(l2)

l2 = sorted(l, reverse=True)
print(l2)

def f(i):
    return 1 % 10

l2 = sorted(l, key=f, reverse=False)
print(l2)