import sys
sys.stdout.write('.');

# 리스트 생성
l = []
l = [1, 2, 'python']

# 인덱싱
print(l[-3], l[-2], l[-1], l[0], l[1], l[2])

# slicing
print('#slicing')
print(l[1:3])
print(l[:])
print(l[2:])
print(l[2::-1]) # Reversing
print(l[len(l)-1::-1]) # Reversing

# 반복
print('# 반복')
l2 = l * 2
print(l2)

# 연결
print('# 연결')
l3 = l + [3, 4, 5]
print(l3)

# 길이
print('# 길이')
print(len(l3))

# 확인
print('# 확인')
print(5 in l3)

# 삭제
print('# 삭제')
print(l3)

# 변경가능한 시퀀스다 (mutable)
print('# 변경가능한 시퀀스다 (mutable)')
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이스를 통한 치환
print('# 슬라이스를 통한 치환')
a = [1, 12, 123, 1234]

a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[2:3] = [30]
print(a)

# 슬라이스를 통한 삭제
print('# 슬라이스를 통한 삭제')
a = [1, 12, 123, 1234]

a[1:2] = []
print(a)

a[0:] = []
print(a)

# 슬라이스를 통한 삽입
print('# 슬라이스를 통한 삽입')
a = [1, 12, 123, 1234]

a[1:1] = ['a']
print(a)

# 마지막 삽입
a[5:] = [12345]
print(a)

# 처음에 삽입
a[:0] = [0]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)

#
# 객체함수 (메서드)
#
print('# 객체함수 (메서드)')
a = [1, 2, 3]

# 맨 뒤 삽입
a.append(5)
print(a)

# 중간삽입
a.insert(1, 2)
print(a)

# 앞에 삽입
a.insert(0,0)
print(a)

# reverse
a.reverse()
print(a)

# 제거
# 값에 의한 제거
a.remove(3)
print(a)

# 위치에 의한 제거
del a[3]
print(a)

# OR

a.pop(3)
print(a)

# 확장
a.extend([-1, -2, -3])
print(a)